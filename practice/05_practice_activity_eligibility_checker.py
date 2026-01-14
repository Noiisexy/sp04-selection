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
You are helping plan a student activity. A student can participate if:

- They are a full-time student, OR
- They are a part-time student AND not working a job

1. Ask the user if they are a full-time student (yes/no)
2. Ask the user if they are a part-time student (yes/no)
3. Ask the user if they have a job (yes/no)
4. Use logic to determine if they can participate
5. Print "You can participate!" or "Sorry, you are not eligible."
'''
# full_time = input("Are you a full-time student? (yes/no) ").lower() 
# part_time = input("Are you a part-time student? (yes/no) ").lower() 
# current_job = input("Do you have a job right now? (yes/no) ").lower()
# if full_time == "yes" or (part_time == "yes" and current_job != "yes"):
#     print("You can participate!")
# else:
#     print("Sorry, you are not eligible.")


full_time = input("Are you a full-time student? (yes/no) ").lower() # full time check
part_time = input("Are you a part-time student? (yes/no) ").lower() # part time check
current_job = input("Do you have a job right now? (yes/no) ").lower() # job status check
if full_time == "yes" and part_time == "no" and current_job == "no": # check if the person is full time student and no job
    print("You can participate!") # display the result
elif part_time == "yes" and current_job == "no": # check if the person is a part time student and no job
    print("You can participate!") # display the result
else:
    print("Sorry, you are not eligible.") # display the result for other answers

