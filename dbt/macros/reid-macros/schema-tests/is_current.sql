{% macro test_is_current(model, column_name, up_to) %}

with max_date as (

    select max( {{column_name}} ) as max_date
    from {{ model }}

),  validation_errors as (

    select * from max_date
    where max_date != {{ up_to }}

)

select
    count(*)
from validation_errors

{% endmacro %}