{% macro grant_access(roles, schema = 'ops_analytics') %}

	{{ slog('Granting access to: ' ~ roles) }}
{% for role in roles %}
    grant usage on schema {{ schema }} to role {{ role }};
    grant select on all tables in schema {{ schema }} to role {{ role }};
    grant select on all views in schema {{ schema }} to role {{ role }};
 {% endfor %}

{% endmacro %}
