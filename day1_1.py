#!python

# https://adventofcode.com/2023/day/1

import re

num = 0
with open('/Users/jasonkendall/Desktop/Advent_of_code/day1_1_input.tx' , mode='r') as fhand:
    for rawline in fhand:
        current_line = rawline.rstrip()
        #print(current_line)
        code = re.sub( '[a-zA-Z]' , '' ,   current_line)
        #print(code)
        num += int( code[0] + code[len(code) - 1 ]  )
        #print(num)
print(num)

