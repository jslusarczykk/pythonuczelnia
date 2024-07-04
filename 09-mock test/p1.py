def f(player1,player2):
    sum1=0
    sum2=0
    for i in range(len(player1)):
        if(player1[i]=="A" or player1[i]=="K" or player1[i]=="Q" or player1[i]=="J" or player1[i]=="T"):
            sum1+=10
        else:
            sum1+=int(player1[i])
    for i in range(len(player2)):
        if(player2[i]=="A" or player2[i]=="K" or player2[i]=="Q" or player2[i]=="J" or player2[i]=="T"):
            sum2+=10
        else:
            sum2+=int(player2[i])

    if(sum1>=sum2):
        return True
    return False
    
print(f("AJ972","AQT72"))
print(f("9532","K8"))
