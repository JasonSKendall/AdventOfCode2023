#!python

import re

# 54699 is the correct answer for day 2 part 2

ohand = open('/Users/jasonkendall/Desktop/Advent_of_code/day2_2_output.txt' , mode='w') 

num = 0
with open('/Users/jasonkendall/Desktop/Advent_of_code/day2_input.txt' , mode='r') as fhand:
#with open('/Users/jasonkendall/Desktop/Advent_of_code/day2_input_test.txt' , mode='r') as fhand:
	#keepGameMax = dict()
	run_sum = 0
	for rawline in fhand:

		#print(file=ohand)
		current_line = rawline.rstrip()

		max_green = 1
		max_red = 1
		max_blue = 1
	
		current_line = re.sub( ' ' , "" , current_line)
		current_line = re.sub( 'green' , "g" , current_line)
		current_line = re.sub( 'red' , "r" , current_line)
		current_line = re.sub( 'blue' , "b" , current_line)
		current_line = re.sub( 'Game' , "" , current_line)

		spltOne = current_line.split(':')

		#game_num = spltOne[0]

		yy = spltOne[1].split(';')

		for i in yy:
			j = i.split(',')
			for k in j:
				if 'r' in k:
					k = int(re.sub( 'r' , "", k))
					if k > max_red:
						max_red = k
				elif 'g' in k:
					k = int(re.sub( 'g' , "", k))
					if k > max_green:
						max_green = k
				elif 'b' in k:
					k = int(re.sub( 'b' , "", k))
					if k > max_blue:
						max_blue = k

		powah = max_red * max_green * max_blue

		run_sum += powah
					
		#zz = { game_num : (max_red , max_green , max_blue, powah, run_sum) }


		#keepGameMax.update(zz)
		
		#print(current_line, file=ohand)

#print(keepGameMax)
ohand.close()
	

print(run_sum)
