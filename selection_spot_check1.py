#kieran burnett
#10-10-2014
#selection spot check 1

grade = int(input("Please enter your pertentage attendance: "))

if grade >= 85:
    print(" Your attendance is {0} %. Keep up the good attendance".format(grade))
elif grade < 85:
    print(" Your attendance is only {0} %. You must improve your attendance.".format(grade))
else:
    print("invalid entry")
