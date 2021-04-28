{% macro view_exists(view, schema) %}
{% set sql %}
select
    exists(
        select
            *
        from information_schema.views s
        where table_name = upper('{{ view }}')
            and table_schema = upper('{{ schema }}')
    )
{% endset %}

{% if execute %}
{{ return(get_exists_value(sql)) }}
{% endif %}
 
{% endmacro %}