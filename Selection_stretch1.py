#Kieran Burnett
#30-09-2014
#Selection statements development exersices 1

month = int(input(" Please enter a month as a number from 1-12: "))
year = int(input(" please enter a year: " ))

#leap years
cent = str(year)[2:4]
if cent == 00:
    leap = year % 400
    if leap == 0:
        print("Leap Year!")
    elif leap != 0:
        print(" Not a leap year!")
else:
    leap = year % 4
    if leap == 0:
        print("Leap year!")
    elif leap != 0:
        print("Not a leap year!")
    else:
        print("Not a leap year!")

#Months
if month == 1:
    print(" January")
elif month == 2:
    print(" February")
elif month == 3:
    print(" March")
elif month == 4:
    print(" April")
elif month == 5:
    print(" May")
elif month == 6:
    print(" June")
elif month == 7:
    print(" July")
elif month == 8:
    print(" August")
elif month == 9:
    print(" September")
elif month == 10:
    print(" October")
elif month == 11:
    print(" November")
elif month == 12:
    print(" December")
else:
    print("Invalid number")
