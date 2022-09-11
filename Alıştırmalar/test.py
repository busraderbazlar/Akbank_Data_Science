how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)

"""names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))"""


"""names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = f"Hi {names},\n\nThis is a reminder that you have {assignments} assignments left to \
submit before you can graduate. You're current grade is {(grades)} and can increase \
to {(int(grade) + int(assignment)*2)} if you submit all assignments before the due date.\n\n"

print (message)

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
"""

with open('\\Users\\PC\\OneDrive\\Masaüstü\\Belgeler\\example_file.txt','r') as f:
    file_data = f.read()
print(file_data)

# note unicoreeror: Typical error on Windows because the default user directory is C:\user\<your_user>, so when you want to pass this path as a string argument into a Python function, you get a Unicode error, just because the \u is a Unicode escape. If the next 8 characters after the \u are not numeric this produces an error. To solve it, just double the backslashes: C:\\user\\<\your_user>... This will ensure that Python treats the single backslashes as single backslashes.