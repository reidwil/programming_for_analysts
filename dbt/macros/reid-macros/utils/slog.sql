{% macro slog(message) %}

	{{ return(log(pretty_time() ~ ' | ' ~ message, true)) }}

{% endmacro %}