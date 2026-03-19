#!/bin/bash

set -euo pipefail
shopt -s nullglob

adl_files=(./*.adl)
if ((${#adl_files[@]} == 0)); then
    echo "No .adl files found in the current directory."
    exit 0
fi

for adl_path in "${adl_files[@]}"; do
    analysis_name=$(basename "$adl_path" .adl)

    if [[ "$analysis_name" == "common" ]]; then
        continue
    fi

    echo "Running analysis: $analysis_name"

    mkdir -p "$analysis_name"
    cp -f "$adl_path" "$analysis_name/"

    cd  "$analysis_name"
    CLA ../../DATA/$analysis_name.13_short.root DELPHES -i "$analysis_name.adl"
    cd ..
done