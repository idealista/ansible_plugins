#!/bin/sh

cd `dirname "$0"`/..
export ANSIBLE_FILTER_PLUGINS=src/filter_plugins
ansible-playbook test/filter_plugins/main.yml