#kieran burnett
#3-10-2014
#selection_devEx4

mark = int(input(" Enter a score: "))

if mark >= 81 and mark <= 100:
    print(" Grade A")
elif mark >= 71 and mark <= 80:
    print(" Grade B")
elif mark >= 61 and mark <= 70:
    print(" Grade C")
elif mark >= 51 and mark <= 60:
    print(" Grade D")
elif mark >= 41 and mark <= 70:
    print(" Grade E")
elif mark <= 40:
    print(" Grade U")
else:
    print("invalid number" )
