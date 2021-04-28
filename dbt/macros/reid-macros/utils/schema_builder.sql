with "columns" as (
	select '- name: ' || column_name  || '\n       description: '|| lower(column_name) || ' (data type '|| lower(DATA_TYPE) || ')'

            as column_statement,
		table_name
	from information_schema.columns
    -- some type of iterative where statement here can get us only the information we need
  order by 1
),
tables as (
select table_name,
'
  - name: ' || table_name || '
    columns:
' || listagg('      ' || column_statement || '\n'|| '\n')  as table_desc
from "columns"
group by table_name
order by table_name
)

select '---Generated automatically, please update after generation
version: 2
sources:
  - name: '  || '
\n\nmodels:' || listagg(table_desc )
from tables;
