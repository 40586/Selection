#kieran burnett
# 7-10-2014
#stretch Ex2

date = int(input("Please enter the date in the format: DdMmYy : with no spaces or breaks"))

day = str(date)[0:2]
month = str(date)[2:4]
year = str(date)[4:6]
#DAY_P


int(year)
#MONTH_P
if month == "01":
    month_p = "January"
elif month == "02":
    month_p = "February"
elif month == "03":
    month_p = "March"
elif month == "04":
    month_p = "April"
elif month == "05":
    month_p = "May"
elif month == "06":
    month_p = "June"
elif month == "07":
    month_p = "July"
elif month == "08":
    month_p = "August"
elif month == "09":
    month_p = "September"
elif month == "10":
    month_p = "October"
elif month == "11":
    month_p = "November"
elif month == "12":
    month_p = "December"
else:
    print("Invalid number")

#YEAR_P
year_p = int(year) + 2000

print(" {0} {1} {2}".format(day,month_p,year_p))
