# create dictionary student_data
# iterate through the dict
# using control flow - if elif - else for loop print all the keys
# print all the values
# print key with matching value name = "zakarie"

student_data = {
    "name": "zakarie",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lessons_names": ["lists", "tuples", "strings"]
}

for x in student_data.values():
    print(x)
for x in student_data:
    # print(x)
    # print(student_1[x])
    if x == "name":
        print(f"Your name is {student_data[x]}")
    elif x == "stream":
        print(f"You study {student_data[x]}")
    elif x == "completed_lessons":
        print(f"You completed {student_data[x]} lessons")




