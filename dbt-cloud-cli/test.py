from src.blob import Blob
from src.dbt import DBT

dbt = DBT()
blob = Blob('dbt-cont')

runs = dbt.list_runs(limit = 2)
for run in runs:
    print(run['id'])