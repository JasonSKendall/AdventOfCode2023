#!sh

# https://adventofcode.com/2023/day/2

cat day2_input.txt | \
	sed 's/ green/g/g' | sed 's/ red/r/g' | sed 's/ blue/b/g' | sed 's/Game //' 

