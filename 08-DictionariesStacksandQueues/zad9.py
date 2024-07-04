countries = [ 
    {"name":"Poland", "population":38000000},
    {"name":"Germany", "population":23432432},
    {"name":"France", "population":532995454},
    {"name":"Ukraine", "population":998845},
    {"name":"Russia", "population":0}
] 

index = 0
while index < len(countries):
    country_data = countries[index]
    print(f"Country: {country_data['name']}, Population: {country_data['population']}")
    index += 1