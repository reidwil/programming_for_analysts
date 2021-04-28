{% macro schema_exists(schema) %}
{% set sql %}
select
    exists(
        select
            *
        from information_schema.schemata s
        where schema_name = upper('{{ schema }}')
    )
{% endset %}

{% if execute %}
{{ return(get_exists_value(sql)) }}
{% endif %}
 
{% endmacro %}
