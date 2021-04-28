# Full Refresh Filter
Author: Reid Williams

A filter that only gets applied in a users `dev` environment incremental models allowing the run command to only build the last N days.

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
