# Author: Angel Le
# GitHub username: lexuanangel
# Date: 1/25/2023
# Description: User will input number of integers to get an output of the
# min and max of integers

print("How many integers would you like to enter?")

# make sure that input is greater than 1
total_integer = int(input())
print(total_integer >= 1)
if total_integer < 1:
    exit()
print("Please enter " + str(total_integer) + " integers.")

# start_num = 0
# while start_num < total_integer:
#     num = int(input())
#     start_num += 1
# set min and maximum integers with placeholders
min_integer, max_integer = 1000, 0

# get numbers and check min and max
for start_num in range(0, total_integer):
    num = int(input())
    # compare for min
    if min_integer > num:
        min_integer = num

    # compare for max
    if max_integer < num:
        max_integer = num
    # for comp_num in num:
    #     print(comp_num)

print("min:", min_integer)
print("max:", max_integer)
