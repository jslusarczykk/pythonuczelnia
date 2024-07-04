def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - 1 - i))
    return decimal

def main():
    binary_input = input("Enter a binary, four-digit number: ")

    if len(binary_input) != 4 or not all(bit in '01' for bit in binary_input):
        print("Invalid input. Please enter a four-digit binary number.")
        return

    decimal_value = binary_to_decimal(binary_input)
    print(f"The decimal equivalent of {binary_input} is {decimal_value}.")

if __name__ == "__main__":
    main()