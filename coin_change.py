# def getWays(n, c):
#     # Complete this function
#     #n= change, c = coins, m = len(c))    
#     def getWays2(n, c, m):
#         if n < 0:
#             return 0
#         if n == 0:
#             return 1
#         # means coins over and n>0 so no solution
#         if m <= 0 and n >= 0:
#             return 0
#         return getWays2(n, c, m - 1) + getWays2(n - c[m-1], c, m)
#     return getWays2(n, c, len(c))
#             
                    
# ways = getWays(4, [1,2,3]) #There are four ways to make change for n = 4
# ways = getWays(10, [2,5,3,6]) #There are four ways to make change for n = 4
# print ways

def getWays(n, c):
    return getWays2(c, len(c), n)

def getWays2(c, m, n):
    table = [0 for k in range(n+1)]
    
    # Base case (If given value is 0)
    table[0] = 1
 
    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0, m):
        for j in range(c[i], n+1):
            table[j] += table[j - c[i]]
 
    return table[n]

# ways = getWays([1,2,3], 4) #There are four ways to make change for n = 4
ways = getWays(10, [2,5,3,6]) #There are four ways to make change for n = 4
print ways