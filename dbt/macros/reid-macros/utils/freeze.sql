{% macro freeze(model, target_schema = "data_science_sandbox", verbose=false) %}

{% set ts = modules.datetime.datetime.now().strftime(format = "%Y%m%d%H%M") %}


{% if execute %}

	{% for node in graph.nodes.values()
	 	| selectattr("resource_type", "equalto", "model") %}

	 	{% if node.name == model %}

	 		{# setting the variables for the table #}
	 		{% set hash_table = "tmp_" ~ ts ~ node.config.alias %}
	 		{% set hash_materialized = node.config.materialized %}

	 		{% if verbose %}
	 		{{ shipt_log_format("Hashed table: " ~ hash_table ~ " | materialized: " ~ hash_materialized) }}
	 		{{ shipt_log_format("Running query now...") }}
	 		{% endif %}

	 		{# Creating the query #}
	 		{% set query %}

	 			create or replace {{hash_materialized}} {{target_schema}}.{{hash_table}} as (select * from {{ ref(model) }})

	 		{% endset %}

	 		{% do log(query, true) %}

	 		{# Running the query #}
	 		{% do run_query(query) %}

	 		{{ shipt_log_format("Create or replace " ~ hash_materialized ~ " " ~ hash_table ~ " has been generated!")}}


		{% endif %}

	 {% endfor %}

{% endif %}


{% endmacro %}

