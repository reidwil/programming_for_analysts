from src.parser import args
from src.dbt import DBT
from src.log import Log
from src.blob import Blob
from src.snowflake import Snowflake

def debug():
    Log("hello")
    dbt = DBT()
    blob = Blob('dbt-cont')
    runs = dbt.list_runs(limit=2)
    print(runs)
    for run in runs:
        Log(f"writing to blob for run {run['id']}")
        blob.write_to_blob(file_name='run_' + {run['id']}, data=run)
    # print(dbt.get_run_results(41938186, to_json=True))


def run() -> str:
    dbt = DBT()
    sf = Snowflake()
    last_insert = sf.get_last_run_insert()
    Log("Getting json payloads from dbt cloud api...")
    jobs = dbt.list_jobs()["data"]
    Log(f"Getting run information with a timestamp greater than: {last_insert}")
    runs = dbt.list_runs(limit=300, order_by="-id")["data"]
    new_runs = []
    run_results = []
    Log("Filtering down to only new runs...")
    for run in runs:
        if dbt.filter_payload_by(run, last_insert):
            Log(f"Found: {run['id']}")
            new_runs.append(run)
            run_results.append(dbt.get_run_results(run["id"]))
    environments = dbt.list_environments()["data"]
    accounts = dbt.list_accounts()["data"]
    projects = dbt.list_projects()["data"]
    Log("Successfully acquired payloads.")

    Log("Connecting to blob and writing files")
    blob = Blob()
    blob.write_to_blob(file_name='run_resuls', data=run_results)

    Log("Connecting to snowflake and copying payloads into raw tables...")
    sf = Snowflake()
    sf.copy_json(run_results, "raw", "dbt", "run_results")
    sf.copy_json(jobs, "raw", "dbt", "job_events")
    sf.copy_json(runs, "raw", "dbt", "run_events")
    sf.copy_json(environments, "raw", "dbt", "environments")
    sf.copy_json(accounts, "raw", "dbt", "accounts")
    sf.copy_json(projects, "raw", "dbt", "projects")
    Log("Successfully copied data to snowflake.")

    Log("Triggering dbt model to build analytics tables...")
    response = dbt.trigger_job_to_run(52680, "Run by Databricks")
    Log.json(response.json()["data"])

def trigger_job(job_id, quiet, poll):
    response = dbt.trigger_job_to_run(job_id, cause="Triggered by dbt-cloud-cli").json()
    if not quiet:
        Log.json(response)
    else:
        Log(f'Job id: {job_id} successfully triggered')
    if poll:
        run_id = response['data']['id']
        dbt.poll(run_id, dbt.on_failure_callback)

def get_run(run_id):
    response = dbt.get_run(run_id)
    Log.json(response)

def get_run_results(run_id):
    response = dbt.get_run_results(run_id)
    Log.json(response)

def stop_run(run_id):
    response = dbt.cancel_run(run_id)
    Log.json(response)


if __name__ == "__main__":
    dbt = DBT()
    blob = Blob('dbt-cont')
    if args.debug:
        debug()
    if args.run:
        run()
    if args.trigger_job:
        trigger_job(args.trigger_job, args.quiet, args.poll)
    if args.get_run_result:
        get_run_results(args.get_run_result)
    if args.stop_run:
        stop_run(args.stop_run)
    if args.get_run:
        get_run(args.get_run)