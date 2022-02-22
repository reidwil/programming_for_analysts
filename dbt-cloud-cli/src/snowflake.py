import json
import snowflake.connector
from snowflake.connector.cursor import SnowflakeCursor
from .config import *


def chunk_data(data: list, size: int = 16384) -> list:
    # Snowflake doesn't like queries longer than 16384 lines
    return [data[x : x + size] for x in range(0, len(data), size)]


class Snowflake(JB_SNOWFLAKE):
    def __init__(self):
        super().__init__()
        if not self.PASSWORD:
            self.engine = snowflake.connector.connect(
                account=self.ACCOUNT,
                user=self.USER,
                authenticator="externalbrowser",
                role=self.ROLE,
                database=self.DATABASE,
                warehouse=self.WAREHOUSE,
            )
        else:
            self.engine = snowflake.connector.connect(
                account=self.ACCOUNT,
                user=self.USER,
                password=self.PASSWORD,
                role=self.ROLE,
                database=self.DATABASE,
                warehouse=self.WAREHOUSE,
            )

    def __repr__(self):
        print(super().__repr__())

    def copy_json(self, data: list, database: str, schema: str, table: str):
        chunks = chunk_data(data)
        sql = f"insert into {database}.{schema}.{table} select parse_json($1), current_timestamp() from values(%s)"
        with self.engine.cursor() as curr:
            try:
                for chunk in chunks:
                    curr.executemany(sql, [json.dumps(payload) for payload in chunk])
            except Exception as e:  # TODO: Create exception classes
                print(f"Exception occured: {e}")
                self.get_last_query_text(curr)

    def get_last_query_text(self, cursor: SnowflakeCursor):
        cursor.execute(
            """
            select query_text
            from table(information_schema.query_history())
            where query_id = (select last_query_id());
            """
        )
        return cursor.fetchone()[0]

    def get_last_run_insert(self):
        with self.engine.cursor() as curr:
            try:
                curr.execute(
                    f"""
                select coalesce(max(metadata_insert_timestamp), '2022-02-01') from {self.DATABASE}.dbt.run_results
                """
                )
                return curr.fetchone()[0]
            except Exception as e:
                print(f"Exception occured: {e}")
                self.get_last_query_text(curr)
