num= int(input("Enter the year:"))
if(num % 4 == 0 and num % 100 != 0) or (num %400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")
