"""
Dbt Cloud API functions
@reid - https://github.com/reidwil
"""
import json
import time
import requests
from requests import Response
from typing import List, Dict
from .config import *
from .wrappers import *


class DBT(DBT_CLOUD):
    def __init__(self):
        super().__init__()
        self.valid_run_results = ["manifest.json", "run_results.json", "catalog.json"]
        self.run_relations = ["trigger", "job", "debug_logs"]

    def __repr__(self):
        return super().__repr__()

    def get(self, url, **kwargs):
        return requests.get(url=url, headers=self.auth_header, **kwargs).json()

    def _write(self, file, item: str) -> str:
        # Appends text to outfile
        with open(file, 'a') as f:
            f.write(item)
        return os.getcwd() + f'/{self.output_file}'

    def _header_output(self) -> str:
        return OUTPUT_HEADER

    def _footer_output(self) -> str:
        return OUTPUT_FOOTER

    def post(self, url, **kwargs):
        self.auth_header["Accept"] = "application/json"
        self.auth_header["Content-Type"] = "application/json"
        return requests.post(url=url, headers=self.auth_header, **kwargs)

    def delete(self, url, **kwargs):
        return requests.delete(url=url, headers=self.auth_header, **kwargs)

    def list_accounts(self) -> List[Dict]:
        return self.get(f"{self.api_base}/api/v2/accounts/")

    def get_account(self, account_id) -> json:
        return self.get(f"{self.api_base}/api/v2/accounts/{account_id}")

    def list_environments(self) -> List[dict]:
        return self.get(f"{self.account_url}/environments/")

    def get_environment(self, environment_id) -> json:
        return self.get(f"{self.account_url}/environments/{environment_id}")

    def list_projects(self) -> List[dict]:
        return self.get(f"{self.account_url}/projects")

    def get_project(self, project_id) -> json:
        return self.get(f"{self.account_url}/projects/{project_id}")

    def list_jobs(self) -> List[dict]:
        return self.get(f"{self.account_url}/jobs/")

    def delete_job(self, job_id: int) -> json:
        return self.delete(f"{self.account_url}/jobs/{job_id}/")

    def update_job(self, job_id: int, **kwargs) -> json:
        payload = self.get_job(job_id=job_id)["data"]
        for key, value in kwargs.items():
            payload[key] = value
        return self.post(f"{self.account_url}/{job_id}/", json=payload)

    def create_job(
        self,
        account_id: int,
        project_id: int,
        environment_id: int,
        name: str,
        execute_steps: List[str],
        **options,
    ):
        # https://docs.getdbt.com/dbt-cloud/api-v2#operation/createJob
        payload = {
            "account_id": account_id,
            "project_id": project_id,
            "environment_id": environment_id,
            "name": name,
            "execute_steps": execute_steps,
        }
        for k, v in options.items():
            payload[k] = v
        return self.post(f"{self.account_url}/jobs/", json=payload)

    def get_job(self, job_id: int) -> Response:
        return self.get(f"{self.account_url}/jobs/{job_id}")

    def filter_payload(self, payload: json) -> Dict:
        """
        Generates the keys necessary for sending a post request to the
        jobs endpoint.
        :params:
        Payload - Takes the output json object from the get_job method
        :returns:
        Dict of payload for sending a post request to update a dbt job
        """
        filtering_keys = [
            "account_id",
            "project_id",
            "environment_id",
            "dbt_version",
            "name",
            "execute_steps",
            "id",
            "triggers",
            "settings",
            "state",
            "generate_docs",
            "schedule",
        ]
        return {k: v for k, v in payload.items() if k in filtering_keys}

    def turn_off_job_schedule(self, job_id: int) -> Response:
        job = self.get_job(job_id)["data"]
        payload = self.filter_payload(job)
        payload["triggers"]["schedule"] = False
        return self.post(f"{self.account_url}/jobs/{job_id}/", data=json.dumps(payload))

    def trigger_job_to_run(self, job_id: int, cause: str, **options) -> json:
        payload = {"cause": cause}
        for k, v in options.items():
            payload[k] = v
        return self.post(
            f"{self.account_url}/jobs/{job_id}/run/", data=json.dumps(payload)
        )

    def cancel_run(self, run_id) -> json:
        return self.post(f"{self.account_url}/runs/{run_id}/cancel/")

    def list_runs(self, **options) -> List[dict]:
        payload = {}
        for key, value in options.items():
            payload[key] = value
        return self.get(f"{self.account_url}/runs/", params=payload)

    def filter_payload_by(
        self, payload: json, filter_date: str, by: str = "created_at"
    ):
        """Takes a payload and filters by a specific criteria from payload"""
        return payload if str(payload[by]) > str(filter_date) else None

    def get_run(self, run_id: int, include_related: List = []) -> json:
        payload = {"include_related": []}
        for item in include_related:
            if item in self.relations:
                payload["include_related"].append(item)
        return self.get(f"{self.account_url}/runs/{run_id}/", params=payload)

    def list_run_artifacts(self, run_id: int, step: int = None) -> List[str]:
        payload = {}
        if step:
            payload["step"] = step
        return self.get(f"{self.account_url}/runs/{run_id}/artifacts/", data=payload)

    def get_run_artifact(self, run_id: int, path: str, step: int = None) -> Response:
        """Returns the artifact give. Must be one of the `valid_run_resuls`"""
        if path not in self.valid_run_results:
            raise Exception(
                f"Given path {path} not in valid results: {self.valid_run_results}"
            )
        payload = {}
        if step:
            payload["step"] = step
        return self.get(
            f"{self.account_url}/runs/{run_id}/artifacts/{path}", data=payload
        )

    def get_run_results(self, run_id: int) -> json:
        try:
            return self.get_run_artifact(run_id, "run_results.json")
        except json.JSONDecodeError:
            print(f"No run results found for run_id: {run_id}")
            return {"run_id": run_id, "data": "No results"}

    def status(self, run_id) -> int:
        response = self.get_run(run_id)
        response_code = response['data']['status']
        return self.run_status_map[response_code]

    def poll(self, run_id: int, callback: callable) -> None:
        status_link = f'{self.api_base}/#/accounts/{self.account_id}/projects/{self.project_id}/runs/{run_id}'
        print(f"Job running - see status here: {status_link}")
        while True:
            status = self.status(run_id)
            print(f"Status -> {status}\t\t({status_link})")
            if status in ['Error', 'Cancelled']:
                callback(run_id, status_link)
                raise Exception(f"Run failed or cancelled. Check: {status_link}")

            if status == 'Success':
                print(f"Success! See details at {status_link}")
                return
            time.sleep(10)

    def on_failure_callback(self, run_id: int, status_link: str):
        """
        Args:
            run_id: integer number of a dbt cloud run id (1234523)
            status_link: the templated string to grab a dbt cloud run (must have run_id in local scope)
        Returns:
            Null

        This method is called during the poll(). It will grab run_results.json and write a nice an github formatted
        file called callback.txt (or whatever)
        """

        self._write(self.output_file, self._header_output())
        self._write(self.output_file, f"### [Link]({status_link})\n\n")

        run_result = self.get_run_results(run_id)
        if run_result["results"]:
            [
            self._write(
                    file = self.output_file,
                    item = f"`{result['unique_id']}`\n```\nError: {result['message']}\n```\n"
                )
                for result in run_result["results"]
                if result['status'] == "error"
            ]
        else:
            self._write(self.output_file, f"```\nCI failed but no run_results.json artifact found.\n```")

        self._write(self.output_file, self._footer_output())