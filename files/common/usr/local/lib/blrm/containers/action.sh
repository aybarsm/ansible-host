#!/usr/bin/env bash

set -euo pipefail

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
POD_NAME=${1:-'UNKNOWN_POD'}
POD_SERVICE=${2:-'UNKNOWN_POD_SERVICE'}
POD_ACTION=${3:-'UNKNOWN_ACTION'}
PATH_DIR_PODS=/home/blrm/pods
PATH_DIR_VAULT=/mnt/vault/containers

PATH_DIR_POD_VAULT="${PATH_DIR_VAULT}/${POD_NAME}"
PATH_DIR_POD="${PATH_DIR_PODS}/${POD_NAME}"

if [ "${POD_ACTION}" == "ExecStartPre" ]; then
    if [ -d "${PATH_DIR_POD_VAULT}" ]; then
        rsync -avzq --no-owner --no-group "${PATH_DIR_POD_VAULT}/" "${PATH_DIR_POD}/"
    fi
elif [ "${POD_ACTION}" == "ExecReload" ]; then
fi

exit 0