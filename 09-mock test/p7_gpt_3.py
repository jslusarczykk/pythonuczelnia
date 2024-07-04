def f(arr):
    count = 0
    for i in range(len(arr)):
        if 4 <= len(arr[i]) <= 12:
            for j in range(len(arr[i])):
                if arr[i][j] == '_' or arr[i][j].isdigit() or ('a' <= arr[i][j] <= 'z'):
                    pass
                else:
                    break
                if j == len(arr[i]) - 1:
                    count += 1
    return count

print(f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]))