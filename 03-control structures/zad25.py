num_products = int(input("Enter the number of purchased products: "))
product_price = float(input("Enter the price of each product: "))

total_price = num_products * product_price

if num_products > 2:
    discount_amount = 0.25 * product_price  
    discount_total = discount_amount * (num_products - 2)  
    total_price -= discount_total

print("The amount to be paid: $", total_price)