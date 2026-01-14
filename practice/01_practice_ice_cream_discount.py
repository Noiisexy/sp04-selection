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
You're working at the BYU Creamery and need to apply a student discount.

1. Ask the user if they are a student (answer "yes" or "no").
2. If they are a student, print "You get a discount!"
3. Otherwise, print "No discount available."
'''
student_validation = input("Are you a student of BYU? (yes/no) ").lower() # validate the student status
if student_validation == "yes": # if the person is a student of BYU
    print("You get a discount!") # give discount
elif student_validation == "no": # if the person is not a student of BYU
    print("No discount available") # deny discount
else: print("unvalid answer") # Any other invalid answers