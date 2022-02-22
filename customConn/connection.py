import snowflake.connector
from snowflake.connector.connection import SnowflakeConnection

class CustomConnection:
    def __init__(self, type, **options):
        self.type = type
        self.__dict__.update(options)
        self.engine = snowflake.connector.connect(
            account = self.account,
            user = self.user,
            password = self.password
        )
        self.cur = self.engine.cursor()

    def __enter__(self):
        yield self.cur

    def __exit__(self, type, value, traceback):
        self.cur.close()

    def __repr__(self) -> str:
        print(f"type = {self.type}\nuser = {self.user}\npass = {self.password}")

    def query_from_str(self, str):
        yield self.cur.execute(str).fetchall()

