#!/usr/env python3
################################################################################
# employee_tracker.py

import sys

# a boolean that will alway be True while our program is running
running = True
# used for our fake authentication system
# note - this is not secure! for demonstrational purposes only
authenticated = False
SYSTEM_TOKEN = "token"

# arrays for the details I want to track
ids = []
names = []
ages = []
notes = []

# get the details of an employee
def get_details():
  input_id = int(input("Enter ID No. \n>"))
  input_name = input("enter name \n>")
  input_age = int(input("enter age \n>"))
  input_note = input("any further comment \n>")

  return (input_id, input_name, input_age, input_note)

# inserts an employee into the array, at a given position
def create(id, name, age, note, ids, names, ages, notes):
  # fails if employee exists
  if len(ids) < id:
    print("create failed, employee exists, exiting...")
    # error code 20 - cannot create, employee exists
    sys.exit(20)
  if len(ids) > id:
    print("create failed, ids cannot be missed, exiting...")
    # error code 21 - cannot create, ids not consecutive
    # all employee ids must be consecutive, so there cannot be missing numbers
    # id: 16, id: 17, id: 20 is illegal (missing id: 19)
    sys.exit(21)
  ids.append(id)
  names.append(name)
  ages.append(age)
  notes.append(note)
  print("create success")
  return (ids, names, ages, notes)

# displays all employee details
def read(ids, names, ages, notes):
  for employee in range(len(ids)):
    print(str(ids[employee]) + "; " + names[employee] + "; "
          + str(ages[employee]) + "; " + notes[employee])
  print("read success")

# replaces an employee
def update(id, name, age, note, ids, names, ages, notes):
  # fails if employee doesn't exist
  if id >= len(ids):
    print("update failed, employee doesn't exist")
    # error code 30 - cannot update/ delete supplied id, has no associated
    # employee
    sys.exit(30)
  ids[id] = id
  names[id] = name
  ages[id] = age
  notes[id] = note
  print("update success")
  return (ids, names, ages, notes)

def delete(id, name, age, note, ids, names, ages, notes):
  # fails if employee doesn't exist
  if id >= len(ids):
    print("delete failed, employee doesn't exist, exiting...")
    # error code 30 - cannot update/ delete supplied id, has no associated
    # employee
    sys.exit(30)
  ids.remove(id)
  names.remove(id)
  ages.remove(id)
  notes.remove(id)
  print("delete success")
  return (ids, names, ages, notes)


while running:
  operation = input("what would you like to do (type help [ENTER]"
                    + " for help with this) \n>")

  # our authentication system
  if not authenticated:
    user_token = input("enter authentication token \n>")
    if user_token != SYSTEM_TOKEN:
      print("authentication failed")
      # error code 1 - authentication error
      sys.exit(1)
    else:
      print("authentacation successful")
      authenticated = True

      # operation should be either create, read, update, delete, help, or
      # quit/ exit, if so do appropriate actions, else prompt again

  if operation == "create":
    id, name, age, note = get_details()
    ids, names, ages, notes = create(id, name, age, note, ids, names, ages, notes)
  elif operation == "read":
    read(ids, names, ages, notes)
  elif operation == "update":
    print("replace the employee at the given id with"
          + " an employee with new details")
    id, name, age, note = get_details()
    ids, names, ages, notes = update(id, name, age, note, ids, names, ages, notes)
  elif operation == "delete":
    id, name, age, note = get_details()
    ids, names, ages, notes = delete(id, name, age, note, ids, names, ages, notes)
  elif operation == "exit" or operation == "quit":
    print("goodbye")
    sys.exit(0)
  else:
    print("operation not recognised")
