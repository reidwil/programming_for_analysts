with CustomConnection('snowflake', snowflake_options) as conn:

    # how the connection could be used
    output = conn.query_from_sql('select id, updated_at from table_1')

    # how to send data into snowflake (if taken from above)
    for id, updated_at in output:

        # we could even call static methods in regards to CustomerConnection
        # like `conn.current_time()`
        conn.query_from_sql(conn, f'''
            insert into table2 (id, updated_at, inserted_at)
            values ('{id}', '{updated_at}', '{conn.current_time()}')
            '''
        )

with CustomConnection('blob', blob_options) as conn:

    # we could do things with blob
    conn.list_files(parititon_key=f'/2021/01/01/')


with CustomConnection('spark', spark_options) as conn:
    # obv we can pass an arbitrary string and some options
    conn.gpu_computer()
