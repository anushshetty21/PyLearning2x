side1=int(input("Enter the side1:"))
side2=int(input("Enter the side2:"))
side3=int(input("Enter the side3:"))
if side1 == side2 and side2 == side3:
    print("It is an Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("It is an Isosceles Triangle")
elif side1 != side2 and side2 != side3:
    print("It is a scalene triangle")
