n = 20
fibonacci_1 = 0
fibonacci_2 = 1

print(fibonacci_1, end=" ")
print(fibonacci_2, end=" ")

for i in range(2, n):
    fibonacci_next = fibonacci_1 + fibonacci_2
    print(fibonacci_next, end=" ")

    fibonacci_1 = fibonacci_2
    fibonacci_2 = fibonacci_next