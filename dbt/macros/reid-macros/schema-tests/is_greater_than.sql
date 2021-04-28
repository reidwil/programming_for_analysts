{% macro test_is_greater_than(model, column_name, date) %}

with less_than as (

    select * 
    from {{ model }}

    where {{ column_name }}::date <= {{ "'" ~ date ~ "'" }}::date

)

select count(*) from less_than

{% endmacro %}
