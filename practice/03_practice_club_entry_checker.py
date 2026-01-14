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
You're checking people into a student event. They must show a student ID
and be on the guest list to get in.

1. Ask the user "Do you have a student ID?" (yes/no)
2. Ask the user "Are you on the guest list?" (yes/no)
3. If both answers are yes, print "Welcome in!"
4. Otherwise, print "Sorry, you can't come in."
'''
ID_validation = input("Do you have a student ID? (yes/no) ").lower() # Validate ID
Guest_validation = input("Are you on the guest list? (yes/no) ").lower() # Valide guest list
if ID_validation and Guest_validation == "yes": # If the person meet two conditions
    print("Welcome in!") # accept
elif ID_validation or Guest_validation == "no": # If the person doesn't meet one condition
    print("Sorry, you can't come in.") # deny
else:
    print("Type the appropriate answer.") # error message display