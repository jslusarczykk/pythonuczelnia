x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

if x > 0 and y > 0:
    print("The point is in the first quadrant")
elif x < 0 and y > 0:
    print("The point is in the second quadrant")
elif x < 0 and y < 0:
    print("The point is in the third quadrant")
elif x > 0 and y < 0:
    print("The point is in the fourth quadrant")
elif x == 0 and y == 0:
    print("The point is at the origin (0,0)")
elif x == 0:
    print("The point is on the y-axis")
elif y == 0:
    print("The point is on the x-axis")
