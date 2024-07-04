price=float(input("What is your price?: "))
discount=float(input("What is your discount?: "))

price2=discount/100*price

print("Price with discount: ",round(price-price2,2))
print(f"Reduction: {round(price2,2)}")