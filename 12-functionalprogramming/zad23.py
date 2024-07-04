arr = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]
#algorythm instructions
#highest and lowest scores are discarded
#sum
arr2 = list(map(lambda x: max(x),arr))
        
print(arr)


arr3 = list(map(lambda x: sum(x),arr))
#print(arr3)
