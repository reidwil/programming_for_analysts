{% macro run_time() %}
    current_timestamp()::TIMESTAMP_NTZ as dbt_run_at
{% endmacro %}
