{% macro clean_ops_stage() %}

{% set table_sql %}
-- tables
select
    table_name
from information_schema.tables
where
    table_schema = 'OPS_STAGE'
    and table_type = 'BASE TABLE'
{% endset %}

{% set table_results = run_query(table_sql) %}
{% set tables = table_results.columns[0].values() %}


{% for table in tables %}
	{% set drop_tables = "drop table prd_datalakehouse.OPS_STAGE." ~ table ~ ";" %}
	{{ slog(drop_tables) }}
	{{ run_query(drop_tables)}}
{% endfor %}

{% set view_sql %}

-- views
select
    table_name
from information_schema.tables
where
    table_schema = 'OPS_STAGE'
    and table_type = 'VIEW'

{% endset %}

{% set view_results = run_query(view_sql) %}
{% set views = view_results.columns[0].values() %}

{% for view in views %}
	{% set drop_views = "drop view prd_datalakehouse.OPS_STAGE." ~ view ~ ";" %}
	{{ slog(drop_views) }}
	{{ run_query(drop_views) }}
{% endfor %}


{% endmacro %}