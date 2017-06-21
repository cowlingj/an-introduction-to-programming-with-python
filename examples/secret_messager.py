#!/usr/bin/env python3
################################################################################
# secret_messager.py

AGENT_1 = "Dave"
AGENT_2 = "Sarah"
AGENT_3 = "Cat the dog"

agent_name = input("Hello agent, what is your codename? ")

SECRET_MESSAGE ="""This is a really long message, dispite it's length, it's
actually quite useless, there isn't much point in reading
this really but here you are agent... still reading...
that's enough now, you can go... please, go away and do
whatever it is agents do... or don't, just keep reading this
instead, you're not even wasting my time anymore, i've moved
on; you shoould too. The only reason you'd still be reading
this is if you thought there was something to gain, well
spoiler alert, there isn't. No secret... No magic words...
No goodies... Nothing................. Still reading?!
I don't have time for this... I quit... For real. Now will
you go? *sigh* I know! QUICK! OVER THERE! *runs away*"""
"""
long comments can also be wrote this way too
great for making them easier to understand
comments like this are ofen at the top of a file to explain how it works, this
is good practice

also good for copying ascii dogs from the internet...
this isn't very good practice

            |`-.__                _=,_
            / ' _/             o_/6 /#\
           ****`               \__ |##/
          /    }                ='|--\
         /  \ /                   /   #'-.
     \ /`   \\\                   \#|_   _'-. /
      `\    /_\\                   |/ \_( # |" 
       `~~~~~``~`                 C/ ,--___/
"""

if agent_name == AGENT_1 or agent_name == AGENT_2 or agent_name == AGENT_3:
  print(SECRET_MESSAGE)
else:
  print("authentication failed")
