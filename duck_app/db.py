import duckdb
import pandas

class DB:
    def __init__(self):
        self.con = duckdb.connect()

    @staticmethod
    def df_to_html(df: pandas.DataFrame):
        return df.to_html(index=False)

    def query_file(self, file, query) -> pandas.DataFrame:
        query = query.replace(":file", f"'{file}'")
        results = self.con.execute(query).df()
        return self.df_to_html(results)
