{% macro database_exists(database) %}
{% set sql %}
select
    exists(
        select
            *
        from information_schema.databases
        where database_name = upper('{{ database }}')
    )
{% endset %}

{% if execute %}
{{ return(get_exists_value(sql)) }}
{% endif %}
 
{% endmacro %}