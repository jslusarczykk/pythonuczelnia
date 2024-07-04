#Enter distance in km: 70
#Enter number of travel hours: 1
#Enter number of travel minutes: 23
#Average speed: 50.6 km/h 
distance = int(input("Enter distance: "))
h = int(input("Enter travel hours: "))
m = int(input("Enter travel minutes: "))

avg_speed = lambda distance,h,m : distance/(h+m/60)
result = round(avg_speed(distance,h,m),2)
print(result)
