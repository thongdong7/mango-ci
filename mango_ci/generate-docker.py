import os
from os.path import join, dirname, exists, abspath

import yaml
from jinja2 import Template


def build_install_cmds(install_cmds):
    ret = []
    for cmd in install_cmds:
        ret.append('%s' % cmd)

    return '\n\n'.join(ret)


def build_before_install_cmds(install_cmds):
    ret = []
    for cmd in install_cmds:
        ret.append('RUN bash -c "%s"' % cmd)

    return '\n\n'.join(ret)


def build_scripts(install_cmds):
    ret = []
    for cmd in install_cmds:
        ret.append('%s' % cmd)

    return '\n\n'.join(ret)


def build_command(config, field_name, method, env, output_field_name):
    if field_name in config:
        if isinstance(config[field_name], str):
            value = [config[field_name]]
        elif isinstance(config[field_name], list):
            value = config[field_name]
        else:
            raise Exception('Invalid command')
    else:
        value = []

    env[output_field_name] = method(value)


def main(source_folder):
    ci_name = '.travis.yml'
    ci_file = join(source_folder, ci_name)
    code_dir = abspath(source_folder)
    output_dir = join(code_dir, '.mango-ci')
    if not exists(output_dir):
        os.makedirs(output_dir)

    config = yaml.load(open(ci_file))

    language = config['language']
    template_dir = join(dirname(__file__), 'templates', language)

    env = {}
    for version in config[language]:
        env[version] = {
            'TRAVIS_%s_VERSION' % (language.upper(),): str(version)
        }

    for version in config[language]:
        # print(python_version)
        params = {
            'version': version,
            'versions': config[language],
            'language': language,
            'code': code_dir,
            'environment': env
        }

        build_command(config, 'before_install', build_before_install_cmds, params, 'before_install_cmds')
        build_command(config, 'install', build_install_cmds, params, 'install_cmds')
        build_command(config, 'script', build_scripts, params, 'script_cmds')

        for root_dir, child_folders, file_names in os.walk(template_dir):
            # print root_dir, child_folders, file_names
            for file_name in file_names:
                file_path = join(root_dir, file_name)
                relative_path = file_path.replace(template_dir + '/', '')
                # print(relative_path)

                template = open(file_path).read()

                content = Template(template).render(**params)
                # print(content)

                output_file = Template(relative_path).render(**params)
                output_path = join(output_dir, output_file)

                if not exists(dirname(output_path)):
                    os.makedirs(dirname(output_path))

                with open(output_path, 'w') as f:
                    f.write(content)
                    # break


if __name__ == '__main__':
    main('/data/projects/subfind-cli')
