

age = 21

if age > 16:
    print("you are old enough to drive")
else:
    print("you cannot drive")


    if age  >= 21:
        print(" you can drive my tesla")
    elif age >= 16:

        print(" you are old enough to drive")
    else:
        print("you should not drive")

# combine conditions with logical operators #
# the logical operators are AND and OR #

if ((age >= 1) and (age <= 18)):
    print(" you get a birthday")

elif ((age == 21)  or (age >= 65)):
    print("you dont get a birthday")