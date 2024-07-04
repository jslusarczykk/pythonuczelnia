def month(n):
    month_names = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    # Check if the input is a valid month number
    if 1 <= n <= 12:
        return month_names[n - 1]
    else:
        return "Invalid month number"
    
print(month(1),month(2),month(11),month(12))