import os
import snowflake.connector

class Snowflake:
    def __init__(self):
        self.conn = snowflake.connector.Connect(
            user = os.getenv('SNOWFLAKE_USER'),
            password = ,
            role = self.credentials.role
        )

    def query_str(self, conn, str, **kwargs):
        # This is a simple way to send information into the method to be queries against our db
        cur = conn.cursor()
        results = cur.execute(str)
        return results

    def copy_to_table(self, blob_path, table, schema, database, **kwargs):
        # This will allow us to copy data from blob to snowflake
        # I think we can copy from blob relative to if the filepath exists in the table already
        query = f"""
        copy into {database}.{schema}.{table}
            from {blob_path}
            storage_integration = myint
            encryption=(type='AZURE_CSE' master_key = {kwargs.get('some azure keys')}')
            file_format = (format_name = my_csv_format);
        """

        res = self.query_str(query)
        return res