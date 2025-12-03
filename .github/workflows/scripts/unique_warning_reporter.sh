#!/bin/bash

# This file determines and counts the unique warnings that appear in the test suite using the
# warnings-as-errors action runs. The volume of each reported warning can be used to indicate
# the severity or importance of rectification.

JOBID=$(gh run list -w "Test-suite with Python warnings as errors" --repo PennylaneAI/pennylane -L 1 --json databaseId -q '.[0].databaseId')
echo "View latest job at https://github.com/PennyLaneAI/pennylane/actions/runs/$JOBID"
gh run view $JOBID --log-failed --repo PennylaneAI/pennylane >/tmp/job_$JOBID.out

cat <<EOF > unique_wae.txt
FutureWarning
pennylane.exceptions.PennyLaneDeprecationWarning
pytest.PytestCollectionWarning
RuntimeWarning
numpy.exceptions.ComplexWarning
pytest.PytestUnraisableExceptionWarning
PendingDeprecationWarning
pytest.PytestRemovedIn9Warning
UserWarning
DeprecationWarning
EOF

declare -A waeCounts

while read -r line; do
    [[ -n "$line" && "$line" != [[:blank:]]* ]] && waeCounts["$line"]=$(grep -F -c "$line" "/tmp/job_$JOBID.out")
done <unique_wae.txt
echo $waeCounts

jsonOut="[{"
for x in "${!waeCounts[@]}"; do
    echo $x :: ${waeCounts[$x]}
    jsonOut+="\"$x\":${waeCounts[$x]},"
done
jsonOut="${jsonOut::-1}}]"
echo $jsonOut >unique_wae.json
