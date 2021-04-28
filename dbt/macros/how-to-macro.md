# Welcome to dbt macros

------------------

### Thoughts

> Though jinja syntax is a bit foreign to most eyes, the implementation with dbt has already proved very useful for our dbt workflows.


### Tips/functionality
- variable substitution: `{{ my_variable }}`
- control flows:
    - if statements: `{% if x = y %} {{ log('x equals y!') }} {% endif %}`
    - loops: `{% for item in list %} {{ item }} {% endfor %}`
- filter data objects:
    - provide default values: `{{ my_variable|default('null') }}`
    - append to lists: `{{ column_list | join(', ') }}`
    - truncate variables: `{{ item | truncate(5) }}`
- uses JinjaSQL templating ([read more](https://github.com/sripathikrishnan/jinjasql))

### Advanced stuff

- identify dbt metadata:
    ```sql
    {% set tables = [] %}

    {% for node in graph.nodes.values() 
        | selectattr("resource_type", "equalto", "model") %}

            {% if node.config.tags == 'public' | lower %}
                {%- do tables.append( node.config.alias ) -%}
                {# or you could use {{ node.config.alias | join(', ') )} #}
            {% endif %}

    {% endfor %}
    ```

- run queries:
    ```sql
    {% set sql %}

    select id
    from my_table

    {% endset %}

    {{ run_query(sql) }}
    ```
- create create macros (think functions in other languages)
    ```python
    {% macro add_two(number) %}

    {{ return (number + 2) }}

    {% endmacro %}
    ```
- reference other macros/pass values from one macro to another
    ```sql
    /* add_two.sql */
    {% macro add_two(number) %}

    {{ return number + 2 }}

    {% endmacro %}
    ```
    ```sql
    /* select123.sql */
    {% macro select_123() %}
    {% set sql %}
    select 1,2,3
    {% endset %}
    {{ run_query(sql) }}
    ```
    ```sql
    /* get_numbers.sql */
    {% set values = select_123() %}
    {% for value in values %}
        {{ add_two(value) }}
    {% endfor %}
    ```
