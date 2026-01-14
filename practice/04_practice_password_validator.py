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
You are building a simple login gate that rejects banned passwords.

1. Ask the user to enter a password.
2. If the password is NOT "1234" or "password", print "Access granted."
3. Otherwise, print "That password is not allowed."
'''
password_input = input("Enter a password: ") # get a value of the password
if password_input == 1234 or password_input == "password": # two passwords are not available
    print("That password is not allowed.") # deny access
else:
    print("Access granted.") # other passwords are accepted