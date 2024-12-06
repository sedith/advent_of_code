#! /bin/bash

no="00$2"
no="${no: -2}"
echo ${no}

folder="$1/$no - $3"
mkdir -p "${folder}"
touch "${folder}/example.txt"
touch "${folder}/input.txt"

touch "${folder}/part_1.py"
echo "import time" > "${folder}/part_1.py"
echo "" >> "${folder}/part_1.py"
echo "" >> "${folder}/part_1.py"
echo "if __name__ == '__main__':" >> "${folder}/part_1.py"
echo "    tic = time.time()" >> "${folder}/part_1.py"
echo "" >> "${folder}/part_1.py"
echo "    with open('example.txt', 'r') as f:" >> "${folder}/part_1.py"
echo "        input = f.read().splitlines()" >> "${folder}/part_1.py"
echo "" >> "${folder}/part_1.py"
echo "" >> "${folder}/part_1.py"
echo "    toc = time.time()" >> "${folder}/part_1.py"
echo "    print('foo:', 0)" >> "${folder}/part_1.py"
echo "    print('time:', toc-tic)" >> "${folder}/part_1.py"

cp "${folder}/part_1.py" "${folder}/part_2.py"

touch "${folder}/README.md"
echo "# Advent of code $1 - Day ${no}: $3" > "${folder}/README.md"
echo "" >> "${folder}/README.md"
echo "## Part 1" >> "${folder}/README.md"
echo "" >> "${folder}/README.md"
echo "" >> "${folder}/README.md"
echo "" >> "${folder}/README.md"
echo "## Part 2" >> "${folder}/README.md"
echo "" >> "${folder}/README.md"
