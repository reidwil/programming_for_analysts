## Incremental filter

### Function args
```jinja2
incremental_filter(
    ref_model, 
    filter_with, 
    comparison = 'dbt_run_at' # this defaults to dbt_run_at (the output of {{ run_time() }})
)
```

### How to use:
```sql
{{
  config(
    alias = 'test_incremental_filter',
    materialized = 'incremental',
    unique_key = 'id'
  )
}}

with orders_after_jan as (

    {{ 
        incremental_filter(
            ref_model = 'src_shipt_og_orders',
            filter_with = 'updated_at'
        )
    }}

)

select 
    id, 
    updated_at, 
    {{ run_time() }} 
from orders_after_jan
```

(this table is actually within `data_science_sandbox` if you want to try that model!)