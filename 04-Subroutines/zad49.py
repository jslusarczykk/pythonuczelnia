def f(dice):
    max_count = 1
    current_count = 1

    for i in range(1, len(dice)):
        if dice[i] == dice[i-1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1

    return max(max_count, current_count)

# Test cases
print(f("5233165554211")) # Output: 5
print(f("2133"))          # Output: 3
