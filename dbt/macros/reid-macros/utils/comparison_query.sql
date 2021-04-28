with old as (

   -- old query is placed here
   select * from {{ ref(old_query) }}

),


new as (
   
   -- new query is placed here
   select * from {{ ref(new_query) }}

),

old_intersect_new as (

    select * from old

    intersect

    select * from new

),


old_minus_new as (

    select * from old

    minus

    select * from new

),


new_minus_old as (

    select * from new

    minus

    select * from old

),


all_records as (

    select

        *,
        true as in_old,
        true as in_new

    from old_intersect_new

    union all

    select

        *,
        true as in_old,
        false as in_new

    from old_minus_new

    union all

    select

        *,
        false as in_old,
        true as in_new

    from new_minus_old

),


summary_stats as (

    select

        in_old,
        in_new,
        count(*) as count_of_rows

    from all_records

    group by 1,2

)


select

    case when in_old and in_new then '✅: perfect match'
         when in_old and not in_new then '🤷: in old only'
         when not in_old and in_new then '🤷: in new only' end as info,
    count_of_rows,
    round(round(100.0 * count_of_rows / sum(count_of_rows) over (), 2)) || '%' as percent_of_total

from summary_stats

order by in_old desc, in_new desc