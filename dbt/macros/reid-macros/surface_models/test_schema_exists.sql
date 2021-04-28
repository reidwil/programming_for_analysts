{% macro test_schema_exists(schema) %}

{% set exists = schema_exists(schema) %}

{% if exists %}
    {{ slog('yay! ' ~ schema ~ ' exists!')}}
{% else %}
    {{ slog('oh nooo! ' ~ schema ~ ' does not exists?!') }}
{% endif %}
 
{% endmacro %}