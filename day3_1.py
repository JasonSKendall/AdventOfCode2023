#!python

import re

# correct answer is 522726
# https://adventofcode.com/2023/day/3


big_long_string = ""
with open('/Users/jasonkendall/Desktop/Advent_of_code/day3_input.txt' , mode='r') as fhand:
#with open('/Users/jasonkendall/Desktop/Advent_of_code/day3_input_test.txt' , mode='r') as fhand:

	for rawline in fhand:
		current_line = rawline.rstrip()

		current_line = "." + current_line + "."

		keep_len = len(current_line)

		current_line = re.sub( '\.' , " " , current_line)
		current_line = re.sub( '[#\&\%\*\$=\+\@_\/\-]' , "Z" , current_line)

		big_long_string += current_line

	

boundary_line = " " * keep_len

big_long_string = boundary_line + boundary_line + big_long_string + boundary_line + boundary_line
print()
print(big_long_string)

locations_to_check = [ -1 , +1 , (- keep_len - 1 ), -keep_len , -keep_len + 1, keep_len -1, keep_len, keep_len + 1]

print()
include_this_number = False
current_number = ""

run_sum = 0

for i,c in enumerate(big_long_string):
	if c == " " or c == "Z":
		if include_this_number:
			run_sum += int(current_number)
			print(current_number)
		include_this_number = False
		current_number = ""
		continue
	if c.isnumeric:
		current_number += c
		#print(i,c)
		for j in locations_to_check:
			k = i + j
			if big_long_string[k] == "Z":
				include_this_number = True


if run_sum == 996543:
	print("TOO HIGH!")
print(run_sum)



