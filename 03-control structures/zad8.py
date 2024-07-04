speed_limit = 140  

def check_speed(speed):
    if speed > speed_limit:
        print("Warning: You have exceeded the speed limit!")
    else:
        print("You are within the speed limit.")

speed = float(input("Enter the car's speed in km/h: "))
check_speed(speed)