def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10 #zapamietac konstrukcje funkcji
        n //= 10
    return sum

if __name__ == "__main__": #sluzy to do importowania bez tego ponizej
    print(sum_digits(7182))
    print(sum_digits(0))
    print(sum_digits(333))


