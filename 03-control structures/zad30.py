time_24 = input("Enter time (24-hour format): ")

hours, minutes = time_24.split(":")

hours = int(hours)

if hours < 12:
    period = "am"
else:
    period = "pm"

hours_12 = hours % 12

print("Time in 12-hour format:", str(hours_12) + ":" + minutes + period)
