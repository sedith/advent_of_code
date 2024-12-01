#! /bin/bash

no="00$2"
no="${no: -2}"
echo ${no}

folder="$1/$no - $3"
mkdir -p "${folder}"
touch "${folder}/example.txt"
touch "${folder}/input.txt"
touch "${folder}/part_1.py"
touch "${folder}/part_2.py"
touch "${folder}/README.md"
echo "# Advent of code $1 - Day ${no}: $3" > "${folder}/README.md"
