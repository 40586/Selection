#kieran burnett
#3-10-2014
#selection-devEx3

hours = int(input(" Please enter the hours you worked this week: "))
pay = int(input(" Please enter your hourly rate: "))

pay_and_half = pay * 1.5
if hours > 60 or hours < 0:
    print(" Nuber entered out of range (0-60)")
elif hours <= 40:
    earned = pay * hours
    print("you have earned: ",earned)
else:
    overtime = hours - 40
    normal_time = hours - overtime
    earned = ( normal_time * pay ) + ( overtime * pay_and_half )
    print("you earned",earned)


