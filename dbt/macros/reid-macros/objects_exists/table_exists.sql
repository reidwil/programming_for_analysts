{% macro table_exists(table, schema) %}
{% set sql %}
select
    exists(
        select
            *
        from information_schema.tables s
        where table_name = upper('{{ table }}')
            and table_schema = upper('{{ schema }}')
    )
{% endset %}

{% if execute %}
{{ return(get_exists_value(sql)) }}
{% endif %}
 
{% endmacro %}