FROM {{language}}:{{version}}

WORKDIR /code

RUN pip install nose

{%- for v1 in environment[version] %}
ENV {{v1}} "{{environment[version][v1]}}"
{% endfor %}

{{before_install_cmds}}

ENTRYPOINT ["/bin/bash", "/entry.sh"]