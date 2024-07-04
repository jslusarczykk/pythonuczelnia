arr=[37,51,44,23,78,92,39,84,83,51] #results

#a >=70 b >=40 c >=30
def min_pts(limit):
    return list(map(lambda pts: pts>=limit, arr))

asses_test = min_pts(70)
print(asses_test(arr))