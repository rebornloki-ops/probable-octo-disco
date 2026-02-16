# ==========================================================
# REPOSITORY: probable-octo-disco
# FILE: dictionaries.py
# DESCRIPTION: My first time diving into Python Dictionaries.
# FUTURE ME: Read the comments to remember how this works!
# ==========================================================

# [cite_start]Defining the initial dictionary with a list inside it [cite: 2]
student = {'name':'John','age':25,'courses':['Math','CompSci']}

# [cite_start]Update function: Changes 'John' to 'Jane', '25' to '26', and adds a phone number [cite: 2]
student.update({'name':'Jane','age':26,'phone':'555-5555'})

# [cite_start]Printing the whole dictionary to see the updates [cite: 2]
print(student)

# [cite_start]Accessing specific data using keys [cite: 2]
print(student['name'])
print(student['courses'])

# [cite_start]Using .get() to avoid errors if a key doesn't exist [cite: 2]
print(student.get('phone','Not Found'))

# [cite_start]Popping (removing) 'age' and storing it to use later [cite: 2]
age = student.pop('age')
print(age)

# [cite_start]Getting metadata: length of dict, all keys, and all items [cite: 2]
print(len(student))
print(student.keys())
print(student.items())

# [cite_start]My first dictionary loop: Iterating through items [cite: 2]
for key in student.items():
    print(key)

# ==========================================================
# END OF SCRIPT - Day 5 Complete
# ==========================================================