![Logo](https://raw.githubusercontent.com/idealista/ansible_plugins/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/ansible_plugins.png)](https://travis-ci.org/idealista/ansible_plugins)

# Ansible Plugins

These are some useful ansible plugins.

- [Getting Started](#getting-started)
  - [Prerequisities](#prerequisities)
  - [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will guide you how to use these plugins in an ansible playbook or role.

### Prerequisities

Python 2.7 installed (at least).
An ansible role or playbook environment.

Plugins are created as [ansible dev guide](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html) says.

### Installing

Just create a folder named **filter_plugins** as says in the [ansible best practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html) and add the file you want.

There are other ways to use them. Check it out the ansible docs.

## Usage

Check out the [test](test) folder to see an example of each plugin.

The provided plugins are:

- [Filter Plugins](src/filter_plugins):
  - [List related](src/filter/plugins/list.py):
    - zip_dict
    - flatten
    - filter
    - filter_evaluated
  - [Collection related](src/filter/plugins/collection.py):
    - in_list
    - not_in_list
    - flatten_collection
  - [String related](src/filter/plugins/string.py):
    -parse_properties

An example of **in_list** plugin filter:

```yml
set_fact:
  list:
    - name: 'one'
      value: 1
    - name: 'two'
      value: 2
    - name: 'three'
      value: 3

set_fact:
  filter_list: ['one', 'two']

set_fact:
  filtered_in_list: "{{ list | in_list('name', filter_list) }}"
```

## Testing

```sh
./test/run.sh
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.4.3.0-green.svg)
![Python](https://img.shields.io/badge/python-2.7-green.svg)

## Versioning

No versions are released in this repository. Master branch has the latest version.

Additionaly you can see what change in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

- **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/ansible_filters/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
