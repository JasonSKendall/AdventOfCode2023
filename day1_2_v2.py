#!python

# https://adventofcode.com/2023/day/1
# part 2

import re


def setnums(i, j, z, k):
    if i == "":
        i = k
        z = True
    else:
        j = k
    return(i,j,z)

ohand = open('/Users/jasonkendall/Desktop/Advent_of_code/output.txt' , mode='w') 

num = 0
with open('/Users/jasonkendall/Desktop/Advent_of_code/day1_input.txt' , mode='r') as fhand:
#with open('/Users/jasonkendall/Desktop/Advent_of_code/day1_input_test.txt' , mode='r') as fhand:
    for rawline in fhand:
        first_num_found = False
        num1 = ""
        num2 = ""

        print(file=ohand)
        current_line = rawline.rstrip()

        print(current_line, file=ohand)
        current_line = re.sub( 'four' , "4" , current_line)
        current_line = re.sub( 'six' , "6" , current_line)

        lencur = len(current_line)
        while current_line:

            print(current_line, num1, num2, file=ohand)
            lencur = len(current_line)

            if current_line[(lencur - 1)].isnumeric() and current_line[0].isnumeric():
                num1 = current_line[0]
                num2 = current_line[(lencur - 1)]
                current_line = ""
                continue


            if current_line[0] not in "123456789eotsfn":
                if lencur > 1:
                    current_line = current_line[1:]
                else:
                    current_line = ""
                continue

            if current_line[0] in "oetsfn":
                if lencur > 4:
                    if current_line[0:5] == "three":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "3")
                        current_line = "3" + current_line[5:]
                        continue
                    if current_line[0:5] == "eight":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "8")
                        current_line = "8" + current_line[5:]
                        continue
                    if current_line[0:5] == "seven":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "7")
                        current_line = "7" + current_line[5:]
                        continue
                if lencur > 3:
                    if current_line[0:4] == "five":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "5")
                        current_line = "5" + current_line[4:]
                        continue
                    if current_line[0:4] == "nine":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "9")
                        current_line = "9" + current_line[4:]
                        continue
                if lencur > 2:
                    if current_line[0:3] == "one":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "1")
                        current_line = "1" + current_line[3:]
                        continue
                    if current_line[0:3] == "two":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "2")
                        current_line = "2" + current_line[3:]
                        continue
                if lencur > 1:
                    current_line = current_line[1:]
                else:
                    current_line = ""
                continue

            if current_line[0].isnumeric():
                if not first_num_found:
                    print("BOING   ...", file=ohand)
                    num1 , num2, first_num_found = setnums(num1, num2, first_num_found, current_line[0])
                    if lencur == 1:
                        current_line = ""
                    continue

            zed = lencur - 1
            if current_line[zed] not in "123456789etno":
                if lencur > 1:
                    current_line = current_line[:-1]
                else:
                    current_line = ""
                continue
            else:
                if lencur > 4:
                    if current_line[-5:] == "three":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "3")
                        current_line = current_line[:lencur-5] + "3"
                        continue
                    if current_line[-5:] == "eight":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "8")
                        current_line = current_line[:lencur-5] + "8"
                        continue
                    if current_line[-5:] == "seven":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "7")
                        current_line = current_line[:lencur-5] + "7"
                        continue
                if lencur > 3:
                    if current_line[-4:] == "five":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "3")
                        current_line = current_line[:lencur-4] + "5"
                        continue
                    if current_line[-4:] == "nine":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "9")
                        current_line = current_line[:lencur-4] + "9"
                        continue
                if lencur > 2:
                    if current_line[-3:] == "one":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "1")
                        current_line = current_line[:lencur-3] + "1"
                        continue
                    if current_line[-3:] == "two":
                        num1 , num2, first_num_found = setnums(num1, num2, first_num_found, "2")
                        current_line = current_line[:lencur-3] + "2"
                        continue
                if lencur > 1:
                    current_line = current_line[:lencur-1]
                    continue


            print("last act...", file=ohand)
            current_line = current_line[1:]


        if num2 == "":
            num2 = num1
        this_num = int(num1 + num2)
        print(this_num, file=ohand)
        num += this_num


print()
if num == 54258 or num == 54288 or num == 54302 or num == 54313 or num == 54341:
    print("Wrong answer:", num )
else:
    print(num)    

ohand.close()
    
