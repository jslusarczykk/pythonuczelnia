 #4 to 12 characters which can be lowercase letters,numbers or underscore
def f(arr): #for given array returns a number of correct words  f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]) = 2
    sum=0
    for i in range(len(arr)):
        if len(arr[i]) > 12 or len(arr[i])<4 :
            continue
        for j in range(len(arr[i])):
            if arr[i][j] == '_' or arr[i][j] == '0' or arr[i][j] == '1' or arr[i][j] == '2' or arr[i][j] == '3' or arr[i][j] == '4' or arr[i][j] == '5' or arr[i][j] == '6' or arr[i][j] == '7' or arr[i][j] == '8' or arr[i][j] == '9' or arr[i][j] == 'a' or arr[i][j] == 'b' or arr[i][j] == 'c' or arr[i][j] == 'd' or arr[i][j] == 'e' or arr[i][j] == 'f' or arr[i][j] == 'g' or arr[i][j] == 'h' or arr[i][j] == 'i' or arr[i][j] == 'j' or arr[i][j] == 'k' or arr[i][j] == 'l' or arr[i][j] == 'm' or arr[i][j] == 'n' or arr[i][j] == 'o' or arr[i][j] == 'p' or arr[i][j] == 'q' or arr[i][j] == 'r' or arr[i][j] == 's' or arr[i][j] == 't' or arr[i][j] == 'u' or arr[i][j] == 'w' or arr[i][j] == 'v' or arr[i][j] == 'x' or arr[i][j] == 'y' or arr[i][j] == 'z':
                pass
            else:
                break
            if j==len(arr[i])-1 :
                sum+=1
    return sum

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))  #is_digit()

#print(isdigit(money[6]))
#print(isdigit(money))