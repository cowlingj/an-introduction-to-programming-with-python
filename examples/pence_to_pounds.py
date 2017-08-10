# pence_to_pounds.py

# ask the user how many pennies they have
pennies = int(input("How many pennies would you like to convert to pounds? "))

# we specify the conversion here to make it clearer what we are doing
# this also makes things easier to change
PENNIES_IN_A_POUND = 100

# work out how much this is in pounds
# n.b in python 3 integer division won't occur without the // operator
#     this saves us having to worry about dividing two integers
pounds = (pennies / PENNIES_IN_A_POUND)

# print the result in a nice form
print(str(pennies) + " = " + str(pounds))
