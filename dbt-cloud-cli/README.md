# dbt cloud cli :cloud:

The name of this repository is slightly a misnomer in the fact that this is really a set of python methods to interact with Jetblue's dbt cloud instance. The `CLI` part of this repository has yet to be set up and possible never will be - if you're reading this and are a master at the [click library](https://click.palletsprojects.com/en/8.0.x/), feel free to contribute :eyes:.

Every method within the DBT class will return either a single json payload or a list of payloads. All of the `DBT.list_*` methods return lists of json payloads


## Dbt Cloud Order of operations :teacher:
`Account` :arrow_right: `Project` :arrow_right: [`Job`, `Environment`] :arrow_right: `Run`

## Usage :raising_hand_woman: :snake:
```python
# From the root of the repo we can import classes
# Here we'll import our dbt class and our logging class
from src.dbt import DBT
from src.log import Log

# Instantiate our dbt class
dbt = DBT()

# Once instantiated we can call any method inside the dbt class
# Some methods require arguments provided as **kwargs

# Let's get all accounts
accounts = dbt.list_accounts()

# Let's get data about job 1
job_1 = dbt.get_job(job_id = 1)['data']

# Using job_1 object above, let's turn off any of its running runs
all_runs = dbt.list_runs()
for run in current_runs['data']:
    if run['job_id'] == job_1['job_id']:
        dbt.cancel_run(run_id = run['run_id'])

# Let's trigger that job to run again
# Let's also change the threads for this run to 20!
response = dbt.trigger_job_to_run(job_id = 1, cause = 'Triggering from dbt-cloud-api', threads = 20)
Log(response)
# 2022-01-15 14:23:03: <[Response 200]>
```

## Env Vars :notebook:
These variables need to be in the environment when trying to run anything within this repository. If one is missing, you will see an error returned like: `KeyError: 'DBT_API_KEY'`. If you are unsure how to set env vars, please refer to docs: [Windows](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html) / [Mac](https://apple.stackexchange.com/questions/106778/how-do-i-set-environment-variables-on-os-x) 

**Dbt Cloud :sun_behind_large_cloud:** - [More info](https://docs.getdbt.com/dbt-cloud/api-v2#section/Authentication)
- DBT_API_KEY
- DBT_ACCOUNT_ID
- DBT_PROJECT_ID

**Snowflake :snowflake:** - [More info](https://docs.snowflake.com/en/user-guide/python-connector-example.html#connecting-using-the-default-authenticator)
- SNOWFLAKE_ACCOUNT
- SNOWFLAKE_DATABASE
- SNOWFLAKE_PASSWORD
  - Optional. If not exists, default to externalbrowser authentication
- SNOWFLAKE_ROLE
- SNOWFLAKE_USER
- SNOWFLAKE_WAREHOUSE


## Sample Output
```json
// From dbt.get_job(45346)
{
    "data": {
        "account_id": 1644,
        "created_at": "2021-12-03T20:38:11.622812+00:00",
        "cron_humanized": "At 00:00 AM, 04:00 AM, 08:00 AM, 12:00 PM, 04:00 PM and 08:00 PM",
        "dbt_version": "0.21.1",
        "deferring_job_definition_id": null,
        "environment_id": 3175,
        "execute_steps": [
            "dbt run -m tag:weather+"
        ],
        "execution": {
            "timeout_seconds": 7200
        },
        "generate_docs": false,
        "generate_sources": false,
        "id": 45346,
        "is_deferrable": false,
        "lifecycle_webhooks": false,
        "lifecycle_webhooks_url": null,
        "name": "DEV - Weather",
        "next_run": "2021-12-15T16:00:00+00:00",
        "next_run_humanized": "1 month",
        "project_id": 2915,
        "run_generate_sources": false,
        "schedule": {
            "cron": "0 0,4,8,12,16,20 * * *",
            "date": {
                "type": "every_day"
            },
            "time": {
                "hours": [
                    0,
                    4,
                    8,
                    12,
                    16,
                    20
                ],
                "type": "at_exact_hours"
            }
        },
        "settings": {
            "target_name": "dev",
            "threads": 4
        },
        "state": 1,
        "triggers": {
            "custom_branch_only": true,
            "git_provider_webhook": false,
            "github_webhook": false,
            "schedule": true
        },
        "updated_at": "2021-12-15T15:35:50.205555+00:00"
    },
    "status": {
        "code": 200,
        "developer_message": "",
        "is_success": true,
        "user_message": "Success!"
    }
}
```