def LongCommonSubs(arr1, arr2):
    maxi = 0
    if len(arr2) > len(arr1):
        lst = [[0 for j in arr2] for k in arr1]
    else:        
        lst = [[0 for j in arr1] for k in arr2]
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            if arr1[i-1] == arr2[j-1]:
                lst[i][j] = lst[i-1][j-1] + 1
            else:
                lst[i][j] = max(lst[i][j-1], lst[i-1][j])
            if lst[i][j] > maxi:
                maxi = lst[i][j]
    print lst
    return lstMax(maxi, arr1)
    
def lstMax(maxi, arr1):
    arr1 = sorted(arr1)
    arr1 = list(set(arr1))
    return arr1[0:maxi]
    
# print LongCommonSubs([1, 2, 3, 4, 1], [3, 4, 1, 2, 1, 3]) #"1 2 3", "1 2 1", "3 4 1" are all correct
print LongCommonSubs( [3, 4, 5], [1, 2, 3, 5]) #"1 2 3", "1 2 1", "3 4 1" are all correct