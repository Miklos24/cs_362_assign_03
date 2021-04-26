year = None
while year == None:
    try:
        print("Please enter a year:")
        year = int(input())
    except ValueError:
        print("Input must be a positive integer\n")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year!")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year!")
else:
    print(year, "is not a leap year.")
