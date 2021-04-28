{% macro swap_schema() %}

    {% set sql='alter schema ops_analytics swap with ops_stage' %}
    {% do run_query(sql) %}
    {{ log("schema swapped", info=True) }}

{% endmacro %}