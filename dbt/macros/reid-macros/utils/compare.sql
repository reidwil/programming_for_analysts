{% macro compare(old_query, new_query) %}

{% set compare_query = compare_queries(
		old_query = old_query,
		new_query = new_query
	)
%}

{% set results = run_query(compare_query) %}

{% if execute %}
{% do results.print_table() %}
{% endif %}

{% endmacro %}