time_24 = input("Enter time (24-hour format): ")

hours, minutes = time_24.split(":")

hours=int(hours)

if_pm=0
if(hours>12):
    if_pm=1
    hours-=12

if(if_pm==1):
    print(f"Your time is {hours}:{minutes}pm")
else:
    print(f"Your time is {hours}:{minutes}am")

