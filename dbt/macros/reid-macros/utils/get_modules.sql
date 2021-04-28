{% macro get_modules(materialization='table', print=false) %}

{% set tables = [] %}

{% for node in graph.nodes.values() 
	| selectattr("resource_type", "equalto", "model") %}

	    {% if node.config.materialized == materialization | lower %}

			{%- do tables.append( node.config.alias ) -%}

		{% endif %}

{% endfor %}

{{ slog(tables) }}

{{ return(tables) }}

{% endmacro %}