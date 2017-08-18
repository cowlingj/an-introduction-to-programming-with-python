# register_writter.py
""" childrensNames.txt file format (one name per line)
Amy Andrews
Brad Benson
...
"""

""" childrensRegister.txt file format
--START--
01/01
Amy Andrews
y
Brad Benson
n
...
--END--
--START--
02/01
...
"""
# first we need to open the name file so we know what the names of the children
# are
childrens_names_file = open("childrensNames.txt", "r")

# create or append to a file the names of children and whether they're present
register_file = open("childrensRegister.txt", "a")

# ask for todays date
date = input("What is today's date? (dd/mm)")

# write the header to the day's entry
register_file.writeline("--START--")
register_file.writeline(date)

# ask whether each child is present and output that information to the register
# file
for name in childrens_name_file
  present = input("is " + name + " present? (y/n)")
  register_file.writelines([name, present])

# close the name file, we don't need it
childrens_name_file.close()

# write the footer for the day's entry
register_file.writeline("--END--")

# close the register file now we're done
register_file.close()
