import datetime
Day = datetime.datetime.now()
Month = datetime.datetime.now()
Year = datetime.datetime.now()

print("\nWhat do u want to know??")

print("\nType day for knowing the Day")

print("\nType month for knowing the Month")

print("\nType year for knowing the Year")

print("\n(Please dont use caps)")

ask = str(input("Enter here: "))

if ask == 'day':
    print(Day.strftime("\n\t%d"))
          
elif ask == 'month':
    print(Month.strftime("\n\t%m"))

elif ask == 'year': 
    print(Year.strftime("\n\t%Y"))
else:
    print("\n\tError:")
