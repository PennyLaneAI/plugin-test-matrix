#!/bin/bash

# This file determines and counts the unique warnings that appear in the test suite using the
# warnings-as-errors action runs. The volume of each reported warning can be used to indicate
# the severity or importance of rectification.

JOBID=$(gh run list -w "Test-suite with Python warnings as errors" --repo PennylaneAI/pennylane -L 1 --json databaseId -q '.[0].databaseId')
echo "View latest job at https://github.com/PennyLaneAI/pennylane/actions/runs/$JOBID"
gh run view $JOBID --log-failed --repo PennylaneAI/pennylane >/tmp/job_$JOBID.out

grep -oE ' [A-Za-z0-9_.]+Warning:' /tmp/job_$JOBID.out | \
    sed 's/^ //' | \
    sed 's/:$//' | \
    sort | \
    uniq -c | \
    awk '{print $2, $1}' > unique_wae.txt

jsonOut="[{"
while read -r name count; do
    echo "$name :: $count"
    jsonOut+="\"$name\":$count,"
done < unique_wae.txt
jsonOut="${jsonOut::-1}}]"
echo $jsonOut >unique_wae.json
