number = int(input("Enter number: "))
def even(x):
    if(x%2==0):
        return True
    else:
        return False

print(f"Number is even: {even(number)}")