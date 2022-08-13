# HOW TO DO TIMING IN PYTHON

# first of all you need to import the time library as such
import time

# then the main line of code that is helpful is this:
moment1 = time.time() * 1000

# time.time() gives us a timestamp
# a timestamp captures a moment in time
# a timestamp is a really big number representing the number of seconds since Jan 1, 1970
# this is the computer's way of telling us the current time
print(moment1) # ... would probably print something like 17682937592.84748323

# normally time.time() is in seconds
# but if you do time.time() * 1000
# its now in milliseconds units
# which lets us be more precise with timing

# generally, we dont care about the numbers in the timestamps themselves
# instead, we care more about taking the DIFFERENCE between timestamps
# which allows us to determine how much time has passed between any two moments

# for example, suppose that this code
moment2 = time.time() * 1000
# runs 1 second later than the code above for moment1

# in that case
time_elapsed = moment2 - moment1

# time_elapsed should be 1000 (in milliseconds), meaning 1 second has passed 

# typically this is used in an if statement in this form
# if moment2 - moment1 >= time_requirement:
#   do_action()

# let's suppose we want something to happen every 5 seconds ... like spawnMushroom()

if time.time() - lastMushroomSpawnTime >= 5000:
  spawnMushroom()
  lastMushroomSpawnTime = time.time() * 1000

# make sure to update the variable tracking when you last performed the action!