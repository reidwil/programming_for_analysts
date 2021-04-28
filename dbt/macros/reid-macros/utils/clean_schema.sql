{% macro clean_schema(schema='OPS_STAGE', debug=false) %}

{% set model_tables = get_modules(materialization='table') %}
{% set model_views = get_modules(materialization='view') %}

{% set missing_tables %}

    select
        table_name
    from PRD_DATALAKEHOUSE.INFORMATION_SCHEMA.TABLES 
    where 
        table_schema = '{{schema}}'
        and table_type = 'BASE TABLE'
        and lower(table_name) not in 
        (
            {%- for table in model_tables -%} 
            {{-"'"~table~"'"-}}
            {%- if not loop.last -%},{% endif %}
            {% endfor %}
        )

{% endset %}

{% set missing_views %}

    select
        table_name
    from PRD_DATALAKEHOUSE.INFORMATION_SCHEMA.TABLES 
    where 
        table_schema = '{{schema}}'
        and table_type = 'VIEW'
        and lower(table_name) not in 
        (
            {%- for view in model_views -%} 
            {{-"'"~view~"'"-}}
            {%- if not loop.last -%},{% endif %}
            {% endfor %}
        )

{% endset %}

{% if execute %}
    {% set table_results = run_query(missing_tables) %}
    {% set drop_tables = table_results.columns[0].values() %}
    {% set view_results = run_query(missing_views) %}
    {% set drop_views = view_results.columns[0].values() %}


    {% if drop_tables is not none %}
        {% for drop_table in drop_tables %}
            {% set query='drop table ' ~ schema ~ '.' ~ drop_table ~ ';' %}
            {% if not debug %}
                {{ slog('Dropping table: ' ~ schema ~ '.' ~ drop_table) }}
                {{ run_query(query) }}
            {% else %}
                {{ slog(query)}}
            {% endif %}
        {% endfor %}
    {% endif %}

    {% if drop_views is not none %}
        {% for drop_view in drop_views %}
            {% set query='drop view ' ~ schema ~ '.' ~ drop_view ~ ';' %}
            {% if not debug %}
                {{ slog("Dropping view: " ~ schema ~ '.' ~ drop_view ) }}
                {{ run_query(query) }}
            {% else %}
                {{ slog(query) }}
            {% endif %}
        {% endfor %}
    {% endif %}
{% endif %}

{{ slog("Done")}}

{% endmacro %}