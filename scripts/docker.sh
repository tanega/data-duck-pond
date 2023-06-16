#!/usr/bin/env bash

set -e

SCRIPT_PATH="$(dirname -- "${BASH_SOURCE[0]}")"

# Pre-pre-flight? 🤷
if [[ -n "$MSYSTEM" ]]; then
    echo "Seems like you are using an MSYS2-based system (such as Git Bash) which is not supported. Please use WSL instead.";
    exit 1
fi

source $SCRIPT_PATH/../docker/.env

if [ "$ENV" == "production" ]; then
    docker compose --project-name=${PROJECT} -f $SCRIPT_PATH/../docker/docker-compose.yml -f $SCRIPT_PATH/../docker/docker-compose.prod.yml "$@"
else
    docker compose --project-name=${PROJECT} --project-directory=$SCRIPT_PATH/../docker "$@"
fi