# stopwatch.py

# we use the time and date time modules from the standard library
# time let's us work out the time something happens
# datetime let's us express it in a readable form
from time import time
import datetime

# here we are just using input to make the program wait until
# the user is ready
input("[ENTER] to start and stop")

# now the user is ready, we can set the start time
start_time = time()

# we again take advantage of the fact input will make the
# program wait
input("running... [ENTER] to stop")

# now we get the stop time
stop_time = time()

# stop time - start time = time elapsed, all we need to do
# is format it nicely
elapsed = datetime.timedelta(0, stop_time - start_time)

# lets print out our results
print("Time Elapsed: " + str(elapsed))
