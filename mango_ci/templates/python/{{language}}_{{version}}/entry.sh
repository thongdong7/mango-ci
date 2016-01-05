#!/usr/bin/env bash

set -o errexit

cd /code

{{install_cmds}}

{{script_cmds}}

echo Completed!!!