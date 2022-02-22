import os
from connection import CustomConnection

sf_options = {
    'user': os.environ.get('SERVICE_SNOWFLAKE_USER'),
    'password': os.environ.get('SERVICE_SNOWFLAKE_PASSWORD'),
    'account': os.environ.get('SNOWFLAKE_ACCOUNT'),
}


with CustomConnection('snowflake', **sf_options) as conn:
    output = conn.query_from_str('select 1')
    print(output)
