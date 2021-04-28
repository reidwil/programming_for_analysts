{% macro unfreeze(tmp_table, type, target_schema = "data_science_sandbox", verbose=false) %}

{% if tmp_table == ''%} {{exceptions.raise_compiler_error("tmp_table argument is empty")}} {% endif %}
{% if type == ''%} {{exceptions.raise_compiler_error("type argument is empty")}} {% endif %}

{% if execute %}

	{{ shipt_log_format("Attempting to unfreeze " ~ tmp_table ~ " from " ~ target_schema) }}

	{% set query %}
		drop {{type}} {{target_schema}}.{{tmp_table}}
	{% endset %}

	{{ shipt_log_format(query) }}

	{% do run_query(query) %}


{% endif %}


{% endmacro %}
