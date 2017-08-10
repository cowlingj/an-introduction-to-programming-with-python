# auto_queue.py

"""
this program simulates waiting in a queue
It prompts for an input which is the starting position and counts down
this simulates the user moving forward in the queue
"""

starting_position = int(input("enter the queue starting position: "))

# the maxamum size of the starting position
QUEUE_LIMIT = 100

# if the starting position is less than or equal to the limit we will count down
if starting_position <= QUEUE_LIMIT:
  # loop as many times as there are queue positions in front
  # (including the start)
  for count in range(starting_position):
    # the output is counting down
    print("you are number " + str(starting_position - count) + " in line")
    # increase the count variable we use to keep track of the number of loops
    # when count becomes larger than the starting position it becomes out of
    # range and the loop stops
    count += 1
  # let the user know when they have finished queuing
  print("thank you, you have reached the front of the queue")
else:
  # let the user know that the queue limit has been exceeded
  print("that's a long queue, auto_queue won't queue that long")
