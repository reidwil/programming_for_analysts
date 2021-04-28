{% macro full_refresh_filter(filter_on, append = false, days_back = '3 days') %}


{% if flags.FULL_REFRESH %}
    {% if target.name == 'dev' %}
        {% if append %}
            and {{ filter_on }} > current_date - interval '{{ days_back }}'
        {% else %}
            where {{ filter_on }} > current_date - interval '{{ days_back }}'
        {% endif %}
    {% endif %}
{% endif %}
 
{% endmacro %}