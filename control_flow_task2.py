# create dictionary student_data
# iterate through the dict
# using control flow - if elif - else for loop print all the keys
# print all the values
# print key with matching value name = "zakarie"

student_data = {
    "name": "zakarie",
    "course": "devops",
    "age": 23,
    "city": "london"
}

for x in student_data.values():
    print(x)
for x in student_data:
    # print(x)
    # print(student_1[x])
    if x == "name":
        print(f"Your name is {student_data[x]}")
    elif x == "course":
        print(f"You are {student_data[x]}")
    elif x == "completed_lessons":
        print(f"You live in {student_data[x]}")




