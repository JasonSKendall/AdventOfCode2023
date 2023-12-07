#!python

import re

# https://adventofcode.com/2023/day/3


def print_the_line_out(z):
	print(len(z))
	max = keep_len
	this_line = ""
	for i,c in enumerate(z):
		if max == 0:
			print(this_line)
			max = keep_len
			this_line = ""
		this_line += c
		max -= 1
		
	


big_long_string = ""

#with open('/Users/jasonkendall/Desktop/Advent_of_code/p' , mode='r') as fhand:
#with open('/Users/jasonkendall/Desktop/Advent_of_code/day3_input_CLEAN.txt' , mode='r') as fhand:
#with open('/Users/jasonkendall/Desktop/Advent_of_code/day3_input_test.txt' , mode='r') as fhand:
with open('/Users/jasonkendall/Desktop/Advent_of_code/day3_input.txt' , mode='r') as fhand:

	for rawline in fhand:
		current_line = rawline.rstrip()

		current_line = "." + current_line + "."

		keep_len = len(current_line)

		current_line = re.sub( '[#\&\%\$=\+\@_\/\-]' , "." , current_line)
		current_line = re.sub( '\*' , "Z" , current_line)

		big_long_string += current_line

	

boundary_line = "." * keep_len 
big_long_string = boundary_line + big_long_string + boundary_line 


off_line_locations_to_check_add_one = [ (True, True, True), (True, False, False), (False, False, True), (True, True, False), (False, True, True) ]
off_line_locations_to_check_add_two =  (True, False, True) 

include_this_number = False
current_number = ""
run_sum = 0
big_long_string_redo = ""


z_keeper = dict()
for i,c in enumerate(big_long_string):
	if c == "Z":
		z_counter = 0

		top_l = i - keep_len - 1
		top_m = i - keep_len 
		top_r = i - keep_len + 1

		bot_l = i + keep_len - 1
		bot_m = i + keep_len 
		bot_r = i + keep_len + 1

		mid_l = i - 1
		mid_r = i + 1

		top_nums = ( big_long_string[top_l].isnumeric() , big_long_string[top_m].isnumeric() , big_long_string[top_r].isnumeric() )
		bot_nums = ( big_long_string[bot_l].isnumeric() , big_long_string[bot_m].isnumeric() , big_long_string[bot_r].isnumeric() )
		lef_num  = big_long_string[mid_l].isnumeric()
		rgt_num  = big_long_string[mid_r].isnumeric()

		if top_nums in off_line_locations_to_check_add_one:
			z_counter += 1
		if top_nums == off_line_locations_to_check_add_two:
			z_counter += 2
		
		if bot_nums in off_line_locations_to_check_add_one:
			z_counter += 1
		if bot_nums == off_line_locations_to_check_add_two:
			z_counter += 2

		if lef_num:
			z_counter += 1

		if rgt_num:
			z_counter += 1

		if z_counter == 2:
			big_long_string_redo += "Z"
			z_keeper[i] = []
		else:
			big_long_string_redo += "."
	else:
		big_long_string_redo += c



#print_the_line_out(big_long_string_redo)


locations_to_check = [ -1 , +1 , (- keep_len - 1 ), -keep_len , -keep_len + 1, keep_len -1, keep_len, keep_len + 1]
include_this_number = False
this_z = -1
run_sum = 0
current_number = ""
big_long_string_redo_with_correct_nums = ""

#print(len(big_long_string_redo))

for i,c in enumerate(big_long_string_redo):
	if c.isnumeric():
		current_number += c
		for j in locations_to_check:
			k = i + j
			if big_long_string_redo[k] == "Z":
				keep_this_z = k
				include_this_number = True
		continue
	
	if len(current_number) > 0:
		if include_this_number:
			#print("keeping it", current_number)
			run_sum += int(current_number)
			z_keeper[keep_this_z].append(int(current_number))
		else:
			current_number = re.sub( '[0-9]' , "." , current_number)
			#print("wiping it out", current_number)
		big_long_string_redo_with_correct_nums += current_number
		current_number = ""
		keep_this_z = 0

	big_long_string_redo_with_correct_nums += c
	include_this_number = False
	current_number = ""
		
#print_the_line_out(big_long_string_redo_with_correct_nums)



run_sum = 0
for key in z_keeper.keys():
	z_prod = z_keeper[key][0] * z_keeper[key][1]
	run_sum += z_prod

print(run_sum)


if run_sum == 81719041 or run_sum == 81321564:
	print("TOO LOW")

if run_sum == 467835:
	print("CORRECT for test data")



