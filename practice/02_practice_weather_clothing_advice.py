'''
OPTIONAL AI GUIDANCE PROMPT:
----------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions to
a practice problem that my professor gave me to try before class. Please be my
kind tutor and walk me through how to solve the problem step by step.

Don't just give me the full solution all at once (unless I later ask for it).
Instead, help me work through it gradually, with clear explanations and small,
easy-to-understand examples. Please use everyday language and explain things
in a simple, friendly way.


INSTRUCTIONS:
-------------
You are making a weather app that gives clothing advice.

1. Ask the user for the temperature (as an integer).
2. If the temperature is below 40, print "Wear a coat."
3. If it's between 40 and 65, print "Wear a jacket."
4. If it's above 65, print "You're good in a t-shirt!"
'''
temperature = int(input("What is the temperature outside? F")) # get a value of the temperature outside from the user
if temperature < 40 :  # if the temperature is below 40 degree
    print("Wear a coat.") # print the recommendation
elif temperature >= 40 and 65 >= temperature : # if the temperature is between 40 and 65
    print("Wear a jacket.") # print the recommendation
elif temperature > 65 : # if the temerature is above 65
    print("You're good in a t-shirt!") # print the recommendation
else:
    print("Sorry, we do not have data for the temperature.") # display the error message