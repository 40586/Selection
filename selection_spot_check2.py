#kieran burnett
#10-10-2014
#selection spot check 2

first_name = input("Please enter your first name ")
last_name = input("Please enter your last name ")
gender = input("Please enter your gender (M/F)")

if gender == "M":
    print(" Mr.{0} {1}".format(first_name,last_name))
elif gender == "F":
    print(" Ms.{0} {1}".format(first_name,last_name))
else:
    print("Please enter an appropriate gender ")
