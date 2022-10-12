#age restriction for movie tickets
# create a condition for 18 & above
# 16 & above
# pg
# 15 & above
# if nothing matched inform the user to enter their age again
# user must not be allowed to enter age over 117 years

print("hi, please input age")
age = int(input(""))
if age > 117:
    print("age must be lower than 117")
elif age >= 18:
    print("allowed to watch all movies")
elif 16 <= age:
    print("allowed movies starting from 16")
elif 12 <= age:
    print("parental guidance is required")
else:
    print("please enter your age again")