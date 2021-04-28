{% macro incremental_filter(ref_model, filter_with, comparison = 'dbt_run_at') %}

    select * from {{ ref(ref_model) }}
    -- just run incremental filtering
    {% if is_incremental() %}
        where {{ filter_with }} >= (select max( {{ comparison }} ) from {{ this }} ) 
    {% endif %}


{% endmacro %}