# Ops Research Macros

Note: some macros run in a query while others are called via the [run-operation](https://docs.getdbt.com/reference/commands/run-operation/) dbt command. Those that are referenced in a query will have a query example while the run-operation examples will have a bash command.

-----------
#### run_time ([source](https://github.com/shipt/ops-research-dbt/blob/master/macros/run_time.sql))
Author: Reid Williams

Universal timestamp generator for dbt runs

**Example**
```sql
select
    id, 
    {{ run_time() }}
from ...
```
**Output**
| id 	| dbt_run_at                 	|
|----	|----------------------------	|
| 1  	| 2021-02-03 12:20:29.939333 	|
| 2  	| 2021-02-03 12:20:29.939333 	|


---------


#### incremental_filter ([source](https://github.com/shipt/ops-research-dbt/blob/master/macros/incremental_filter/incremental_filter.sql))
Author: Reid Williams

Template to write incremental CTEs.

**Args**

* `ref_model` (required): model name the incremental filter should be applied to.
* `filter_with` (required): timestamp column to compare dbt_run_at to.
* `comparison` (optional): column to compare the `filter_with` against. Defaults to `dbt_run_at`

**Example**
```sql
{{
  config(
    materialized = 'incremental'
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
    *
    {{ run_time() }} 
from orders_after_jan
```

----------

#### full_refresh_filter ([source](https://github.com/shipt/ops-research-dbt/blob/master/macros/full_refresh_filter/full_refresh_filter.sql))
Author: Reid Williams & Justin Farnish

A filter that only gets applied in a users `dev` environment. Affects incremental models allowing the run command to only build the last N days (as opposed to all pieces of data).

**Args**
* `filter_on` (reguired): The column to filter upon
* `append` (required, default: `FALSE`): Should this macro be appended to preexisting `where` statement or not
* `days_back` (optional, default: `'3 days'`): How many days back should we filter

**Example**

```sql
{{
    config(
        materialization = 'incremental',
        unique_key = 'id'
    )
}}

select * from my_huge_cte

where ...

{{ full_refresh_filter('updated_at', append = true) }}
```

--------

#### surface_models_to_schema ([source](https://github.com/shipt/ops-research-dbt/blob/master/macros/surface_models_to_schema.sql))
Author: Reid Williams

Run time macro to be called after other `dbt run` calls that surface all models with a `public` tag in their config to a specified schema.

**Args**
`schema` (optional): string of a schema to surface models to. default = `DATA_SCIENCE`

**Example**

`$ dbt run-operation surface_models_to_schema`
or
`$ dbt run-operation surface_models_to_schema --args '{schema: 'NAME_OF_SCHEMA'}'`

**Caveats**
- This lazily writes the view using `create view ... as (select * from ...)`. Because of this, adding a new field into the model will cause the created view to break with `expected N columns got M columns`. To fix:

  - Adjust the macro to explicitly write the column names in the view creation instead of `*` **(okay option)**

  or:

  - Write a macro that checks `state:modified` and if any of the models flagged as `modified` have a `public` tag, trigger `surface_models_to_schema` in the `post-run-hook` **(better option)**

-----

#### grant_access ([source](https://github.com/shipt/ops-research-dbt/blob/master/macros/grant_access.sql))

Author: Reid Williams

Loops over a list of snowflake/shipt specific roles and grants them access to the provided schema. This macro should generally be applied as a [on-run-end](https://docs.getdbt.com/docs/building-a-dbt-project/hooks-operations/#hooks) hook in your `dbt_project.yml`.

**Args**
* `roles` (required): pythonic list of roles to grant access to
    * it is recommended to define the list of roles as a [var](https://docs.getdbt.com/docs/building-a-dbt-project/building-models/using-variables/) in your `dbt_project.yml` - [example](https://github.com/shipt/ops-research-dbt/blob/master/dbt_project.yml#L21)
* `schema` (optional): specific schema to grant access to. default=`ops_analytics`

**Example**

`dbt_project.yml`
```yaml
...

vars:
    roles: ["role1", "role2"]

on-run-end:
    - "{{ grant_access(var('roles')) }}
    
...
```
or
`$ dbt run-operation grant_access --args '{roles: ['role1','role2']}'`
