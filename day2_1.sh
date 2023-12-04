#!sh

# https://adventofcode.com/2023/day/2
# 2593 is the correct answer...

cat day2_input.txt | \
	sed 's/ green/g/g' | sed 's/ red/r/g' | sed 's/ blue/b/g' | sed 's/Game //' | \
	sed 's/[;,:]/ /g' | sed 's/$/ /' | \
	sed 's/ [0-9][rgb] / /g'  | \
	sed 's/ 1[012]r/ /g' | \
	sed 's/ 1[0123]g //g' | \
	sed 's/ 1[01234]b //g' | \
	egrep -v '[bgr]' | \
	awk '{sum+=$1;} END{print sum;}'

