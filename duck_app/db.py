import duckdb
import pandas

class DB:
    def __init__(self):
        self.con = duckdb.connect()
    @staticmethod
    def df_to_html(df: pandas.DataFrame):
        return df.to_html(index=False)

    def query_file(self, file) -> pandas.DataFrame:
        results = self.con.execute(f"select * from '{file}'").df()
        return self.df_to_html(results)
