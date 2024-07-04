stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
#Write a program that calculates the total value of products in stock.
#  Use the map(), sum() and anonymous function
#Products in stock: [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
#Total value: 423.35
print(stock)
total_value=sum(map(lambda x: x[0]*x[1], stock))
print(total_value)
