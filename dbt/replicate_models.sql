{% macro surface_models_to_schema(schema, verbose = true) %}

{%- if schema is not defined -%}
    {%- set error_message -%}
        Schema argument is not set. 
        Expected call: 
        $ dbt run-operation test_it --args '{schema: <specify_schema>}'
    {%- endset -%}
    {{ exceptions.raise_compiler_error(error_message) }}
{% endif %}

{% set exists = schema_exists(schema) %}
{% if execute and not exists %}
    {% set create_schema_if_not_exists = create_schema(schema) %}
    {% if verbose %}
        {{ slog('Schema does not exists. Creating now...') }}
    {% endif %}
    {{ run_query(create_schema_if_not_exists) }}
{% endif %}


{% set models = [] %}
{% for node in graph.nodes.values() | selectattr("resource_type", "equalto", "model") %}
    {% if 'public' in node.config.tags %}
        {%- do models.append(node) -%}
    {% endif %}
{% endfor %}


{% for model in models %}
    {% set columns = [] %}
    {%- do columns.append(get_columns_in_query("select * from " ~ model.database ~ '.' ~ model.schema ~ '.' ~ model.alias)) -%}
    {% set sql %}
        create or replace view {{ model.database }}.{{ schema }}.{{ model.alias }} as (
            select 
            {% for column in columns[0] %}
            "{{ column }}"{% if not loop.last %} , {% endif %}
            {% endfor %} 
            from {{ model.database }}.{{ model.schema }}.{{ model.alias }}
        );
    {% endset %}
    {% if verbose %}
        {{ slog("Creating view for " ~ model.schema | lower ~ '.' ~ model.alias ~ " within " ~ schema) }}
    {% endif %}
    {% if execute %}
        {{ run_query(sql) }}
    {% endif %}
{% endfor %}

{{ slog('Created ' ~ models | length ~ ' views(s) in ' ~ schema) }}

{% endmacro %}
