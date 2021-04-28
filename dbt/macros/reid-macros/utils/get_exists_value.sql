{% macro get_exists_value(sql) %}
    {% set output = run_query(sql) %}
    {% set value = output.columns[0].values()  %}
    {{ return(value[0] | as_bool) }}
{% endmacro %}