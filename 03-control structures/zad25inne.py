num_products = int(input("Enter the number of purchased products: "))
product_price = float(input("Enter the price of each product: "))

suma=num_products*product_price

if(num_products>2):
    discount=product_price*0.25
    total_discount=(num_products-2)*discount
    suma-=total_discount

print(suma)