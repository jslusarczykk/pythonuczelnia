ean_number = int(input("Enter EAN-13 article number: "))

if len(ean_number) == 13:
    print("Article number is correct")
    
    if ean_number[:3] == '590':
        print("Article manufactured in Poland")
else:
    print("Invalid EAN-13 article number")