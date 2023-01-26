# Author: Angel Le
# GitHub username: lexuanangel
# Date: 1/25/2023
# Description: User inputs positive integer to get an output of all factors

pos_int = int(input("Please enter a positive integer: "))
# Made so that the value exits if its smaller than 0 or negative
if pos_int < 0:
    exit()
print("The factors of", pos_int, "are: ")

# to make sure to get all the factors
for factor_int in range(1, pos_int + 1):
    if pos_int % factor_int == 0:
        print(factor_int)

# This was my previous trials, it did not go well.
# try to expand the range
# factor_int += 1
# pos_integer = int(input())
# print("Please enter a positive integer: " + str(pos_integer))
# even_integer = pos_integer / 2
# we want this to go through all the factors of the number
# for even_integer in pos_integer:
# print(even_integer)
# odd_integer = pos_integer
# while even_integer:
# print(even_integer)
# even_integer += 2
# print(even_integer)
# factor_int = int(pos_integer % 2)
# factor_int = int(pos_integer % 2)
# remainder = pos_integer % factor_int
# floor division?
# print(factor_int)
# The factors of 12 are:
