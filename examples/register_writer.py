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
register_file.write("--START--\n")
register_file.write(date + "\n")
# ask whether each child is present and output that information to the register
# file
for name in childrens_names_file:
  present = input("is " + name + " present? (y/n)")
  register_file.writelines([name, present + "\n"])

# close the name file, we don't need it
childrens_names_file.close()

# write the footer for the day's entry
register_file.write("--END--\n")

# close the register file now we're done
register_file.close()
