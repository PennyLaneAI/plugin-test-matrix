#!/bin/bash

# This file determines and counts the unique warnings that appear in the test suite using the
# warnings-as-errors action runs. The volume of each reported warning can be used to indicate
# the severity or importance of rectification.

JOBID=$(gh run list -w "Test-suite with Python warnings as errors" -L 1 --json databaseId -q '.[0].databaseId')
echo "View latest job at https://github.com/PennyLaneAI/pennylane/actions/runs/$JOBID"
gh run view $JOBID --log-failed >/tmp/job_$JOBID.out
cat /tmp/job_$JOBID.out | grep "Warning:" | awk '{split($0,a,"Warning:"); print a[1]"Warning"}' | awk '{split($0,a," - "); print a[2]}' | sort -u >unique_wae.txt

declare -A waeCounts

while read -r line; do
    [[ -n "$line" && "$line" != [[:blank:]]* ]] && waeCounts["$line"]=$(cat /tmp/job_$JOBID.out | grep "$line" | wc -l)
done <unique_wae.txt
echo $waeCounts

jsonOut="[{"
for x in "${!waeCounts[@]}"; do
    echo $x :: ${waeCounts[$x]}
    jsonOut+="\"$x\":${waeCounts[$x]},"
done
jsonOut="${jsonOut::-1}}]"
echo $jsonOut >unique_wae.json
