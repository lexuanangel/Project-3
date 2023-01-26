# Author: Angel Le
# GitHub username: lexuanangel
# Date: 1/25/2023
# Description: User inputs positive integer to get an output of all factors

pos_int = int(input("Please enter a positive integer: "))
print("The factors of 12 are: " + str(pos_int))

# to make sure to get all the factors
for factor_int in range(1, pos_int + 1):
    if pos_int % factor_int == 0:
        print(factor_int)
# try to expand the range
    factor_int += 1

# This was my previous trials, it did not go well.
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
