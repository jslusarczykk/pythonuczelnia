def f(arr):
    count = 0
    for word in arr:
        if 4 <= len(word) <= 12:
            valid_word = True
            for char in word:
                if not ('a' <= char <= 'z' or '0' <= char <= '9' or char == '_'):
                    valid_word = False
                    break
            if valid_word:
                count += 1
    return count

print(f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]))