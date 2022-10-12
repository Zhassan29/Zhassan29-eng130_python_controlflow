#

data = 0

#while data < 10:
#    print(f"its working - >{data}")
 #   if data == 5:
 #       break # key word
 #   data += 1


user_prompt = True

while user_prompt:
    age = input("please enter your age")
    if age.isdigit():
        user_prompt = False
    else:
        print("please enter your age in digits only")
print("your age is {age}")
