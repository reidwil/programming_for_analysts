import os
from dataclasses import dataclass
from typing import Optional

ARTIFACT_FILE = "run_results.json"


@dataclass
class DBTCONFIG:
    output_file: str
    api_base: str
    job_cause: str
    git_branch: str
    api_key: str
    account_id: str
    project_id: str
    auth_header: str
    account_url: str
    project_url: str
    run_status_map: dict


class DBT_CLOUD(DBTCONFIG):
    def __init__(self):
        self.output_file = 'callback.txt'
        self.api_base = os.environ.get(
            "DBT_URL", "https://cloud.getdbt.com"
        )  # default to multitenant url
        self.job_cause = os.environ.get(
            "DBT_JOB_CAUSE", "Test"
        )  # default to generic message
        self.git_branch = os.environ.get("GITHUB_REF", None)  # default to None
        self.api_key = os.environ[
            "DBT_API_KEY"
        ]  # no default here, just throw an error here if key not provided
        self.account_id = os.environ[
            "DBT_ACCOUNT_ID"
        ]  # no default here, just throw an error here if id not provided
        self.project_id = os.environ[
            "DBT_PROJECT_ID"
        ]  # no default here, just throw an error here if id not provided
        self.auth_header = {"Authorization": f"Token {self.api_key}"}
        self.account_url = f"{self.api_base}/api/v2/accounts/{self.account_id}"
        self.project_url = f"{self.account_url}/projects/{self.project_id}"
        self.run_status_map = {
            1: "Queued",
            2: "Starting",
            3: "Running",
            10: "Success",
            20: "Error",
            30: "Cancelled",
        }


@dataclass
class SNOWFLAKECONFIG:
    ACCOUNT: str
    DATABASE: str
    PASSWORD: Optional[str]
    ROLE: str
    USER: str
    WAREHOUSE: str


class SNOWFLAKE(SNOWFLAKECONFIG):
    def __init__(self):
        self.ACCOUNT = os.environ.get("SNOWFLAKE_ACCOUNT")
        self.DATABASE = os.environ.get("SNOWFLAKE_DATABASE")
        self.PASSWORD = os.environ.get("SNOWFLAKE_PASSWORD")
        self.ROLE = os.environ.get("SNOWFLAKE_ROLE")
        self.USER = os.environ.get("SNOWFLAKE_USER")
        self.WAREHOUSE = os.environ.get("SNOWFLAKE_WAREHOUSE")
