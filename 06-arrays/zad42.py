import random

def rand_elem(arr):
    return arr[random.randint(0,len(arr)-1)]

number_table = [3, 8, 12, 5, 21, 9, 15, 4, 11, 7,
                30, 6, 18, 13, 25, 2, 17, 22, 14, 10,
                35, 19, 27, 1, 20, 16, 28, 33, 26, 40,
                23, 37, 29, 44, 32, 38, 24, 42, 36, 45,
                49, 31, 46, 34, 41, 48, 39, 50, 43, 47]

print(rand_elem(number_table),end=" ")
print(rand_elem(number_table),end=" ")
print(rand_elem(number_table),end=" ")