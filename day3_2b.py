#!python

import re

# https://adventofcode.com/2023/day/3


def print_gear_list():
	for i in gear_list:
		print(i)
	print()

gear_list = []

#with open('/Users/jasonkendall/Desktop/Advent_of_code/day3_input_test.txt' , mode='r') as fhand:
with open('/Users/jasonkendall/Desktop/Advent_of_code/day3_input.txt' , mode='r') as fhand:
	i = 0
	for rawline in fhand:
		current_line = rawline.rstrip()
		gear_list.append([])
		gear_list[i].append(".")
		for c in current_line:
			if c.isnumeric():
				gear_list[i].append(c)
			elif c == "*":
				gear_list[i].append("Z")
			else:
				gear_list[i].append(".")
		gear_list[i].append(".")
		i += 1

keep_len = len(gear_list[0])
boundary_list = ['.'] * keep_len 
big_long_gear_list = [boundary_list] + gear_list + [boundary_list]
gear_list = big_long_gear_list

#print_gear_list()


locations_to_check = [ 
( True , False , False , True , False, False, False, False ) ,
( True , False , False , False, True , False, False, False ) ,
( True , False , False , False, False, True, False, False ) ,
( True , False , False , False, False, True, True, False ) ,
( True , False , False , False, False, True, True, True ) ,
( True , False , False , False, False, False, True, True ) ,
( True , False , False , False, False, False, False, True ) ,

( True , True , False , True , False, False, False, False ) ,
( True , True , False , False, True , False, False, False ) ,
( True , True , False , False, False, True, False, False ) ,
( True , True , False , False, False, True, True, False ) ,
( True , True , False , False, False, True, True, True ) ,
( True , True , False , False, False, False, True, True ) ,
( True , True , False , False, False, False, False, True ) ,

( True , True , True , True , False, False, False, False ) ,
( True , True , True , False, True , False, False, False ) ,
( True , True , True , False, False, True, False, False ) ,
( True , True , True , False, False, True, True, False ) ,
( True , True , True , False, False, True, True, True ) ,
( True , True , True , False, False, False, True, True ) ,
( True , True , True , False, False, False, False, True ) ,

( False , True , True , True , False, False, False, False ) ,
( False , True , True , False, True , False, False, False ) ,
( False , True , True , False, False, True, False, False ) ,
( False , True , True , False, False, True, True, False ) ,
( False , True , True , False, False, True, True, True ) ,
( False , True , True , False, False, False, True, True ) ,
( False , True , True , False, False, False, False, True ) ,

( False , False , True , True , False, False, False, False ) ,
( False , False , True , False, True , False, False, False ) ,
( False , False , True , False, False, True, False, False ) ,
( False , False , True , False, False, True, True, False ) ,
( False , False , True , False, False, True, True, True ) ,
( False , False , True , False, False, False, True, True ) ,
( False , False , True , False, False, False, False, True ) ,

( False , False , False , True , False,  True, False, False ) ,
( False , False , False , False, True,   True, False, False ) ,
( True , False , False , False, False,   True, False, False ) ,
( True , True , False , False, False,    True, False, False ) ,
( True , True , True , False, False,     True, False, False ) ,
( False , True , True , False, False,    True, False, False ) ,
( False , False , True , False, False,     True, False, False ) ,

( False , False , False , True , False,  True, True, False ) ,
( False , False , False , False, True,   True, True, False ) ,
( True , False , False , False, False,   True, True, False ) ,
( True , True , False , False, False,    True, True, False ) ,
( True , True , True , False, False,     True, True, False ) ,
( False , True , True , False, False,    True, True, False ) ,
( False , False , True , False, False,     True, True, False ) ,

( False , False , False , True , False,  True, True, True ) ,
( False , False , False , False, True,   True, True, True ) ,
( True , False , False , False, False,   True, True, True ) ,
( True , True , False , False, False,    True, True, True ) ,
( True , True , True , False, False,     True, True, True ) ,
( False , True , True , False, False,    True, True, True ) ,
( False , False , True , False, False,     True, True, True ) ,

( False , False , False , True , False,  False, True, True ) ,
( False , False , False , False, True,   False, True, True ) ,
( True , False , False , False, False,   False, True, True ) ,
( True , True , False , False, False,    False, True, True ) ,
( True , True , True , False, False,     False, True, True ) ,
( False , True , True , False, False,    False, True, True ) ,
( False , False , True , False, False,     False, True, True ) ,

( False , False , False , True , False,  False, False, True ) ,
( False , False , False , False, True,   False, False, True ) ,
( True , False , False , False, False,   False, False, True ) ,
( True , True , False , False, False,    False, False, True ) ,
( True , True , True , False, False,     False, False, True ) ,
( False , True , True , False, False,    False, False, True ) ,
( False , False , True , False, False,     False, False, True ) ,

( False , False , False , True , True,  False, False, False ) ,
( True , False , True , False , False,  False, False, False ) ,
( False , False , False , False , False,  True, False, True ) 

]




include_this_number = False
current_number = ""
run_sum = 0
big_long_string_redo = ""


z_keeper = dict()
for i in range(len(gear_list)):
	for j in range(len(gear_list[i])):
		z_counter = 0
		if gear_list[i][j] == "Z":

			top_l = gear_list[i-1][j-1].isnumeric()
			top_m = gear_list[i-1][j].isnumeric()
			top_r = gear_list[i-1][j+1].isnumeric()

			bot_l = gear_list[i+1][j-1].isnumeric()
			bot_m = gear_list[i+1][j].isnumeric()
			bot_r = gear_list[i+1][j+1].isnumeric()

			mid_l = gear_list[i][j-1].isnumeric()
			mid_r = gear_list[i][j+1].isnumeric()

			if ( top_l , top_m , top_r , mid_l , mid_r, bot_l, bot_m, bot_r ) in locations_to_check:
				z_keeper[(i,j)] = []
			else:
				gear_list[i][j] = "."



#print_gear_list()


for i in range(len(gear_list)):
	current_number = []
	include_this_number = False
	this_i = -99
	this_j = -99
	for j in range(len(gear_list[i])):
		if gear_list[i][j].isnumeric():
			current_number.append(j)
			for m in i-1, i, i+1:
				for n in j-1, j, j+1:
					if gear_list[m][n] == "Z":
						include_this_number = True
						this_i = m
						this_j = n
			continue
	
		if len(current_number) > 0:
			current_num_str = ""
			if include_this_number:
				for q in current_number:
					current_num_str += gear_list[i][q]
				final_num = int(current_num_str)
			for q in current_number:
				gear_list[i][q] = "."
			if include_this_number:
				z_keeper[(this_i , this_j)].append(final_num)

			final_num = -99
			current_number = []
			include_this_number = False


#print_gear_list()

print(z_keeper)

run_sum = 0
for key in z_keeper.keys():
	z_prod = z_keeper[key][0] * z_keeper[key][1]
	run_sum += z_prod

print(run_sum)


if run_sum == 81719041 or run_sum == 81321564:
	print("TOO LOW")

if run_sum == 467835:
	print("CORRECT for test data")



