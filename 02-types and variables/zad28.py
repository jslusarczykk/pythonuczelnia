height=float(input("What is your height?: "))
weight=float(input("What is your weight?: "))

height=height/100

bmi=weight/(height**2)

print(f"Twoje bmi to: {bmi}")
if(bmi>18.49 and bmi<30.0):
    print("Twoja waga jest prawidlowa")
else:
    print("Twoja waga jest nieprawidlowa")
