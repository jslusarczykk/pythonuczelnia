
current_price = float(input("Enter the current product price: "))
previous_price = float(input("Enter the previous product price: "))

price_decrease = (previous_price-current_price)/previous_price*100 

if price_decrease >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_decrease} %")
else:
    print("Do not buy the product. Insufficient price decrease.")