# Importing standard libraries
'''
    1. Adding choclates to everyone else except one by a number N is equal 
    to subtracting choclates from that one person by N. This is because we
    only are concerned with OPERATIONS for equalizing number of choclates 
    of everybody.
    2. There is an optimum minimum level.(minimum number of chochlates).
    This can be either the min of the entire numbers of choclates with peo
    -ple initially, or anything in range [fMin, fMin - 5]. It can't go bey
    -ond that because it will always require an extra operation since the
    max greedy reaching way(subtraction amount of choclates) is 5.
    3. for any level between fMin to fMin - 5, we make each person reach
    there by subtracting chocolates in a greedy way. Say if the chocs ini
    -tially are k, we reach by k/5 + (k%5)/2 + (k%5)%2 . We compute such
    steps for all people are compute total number of operations in this way.
    FINALLY, we do this for the range fMin to fMin - 5 and compute the
    min of this and return this as the answer.    
'''

def getMinOper(Arr):
    Arr.sort()
    minVal = Arr[0]
    results = []
    for i in range(minVal-5, minVal+1):
        results.append(getMin(Arr, i))
    return min(results)
    
def getMin(Arr, minVal):
    count = 0
    for i in Arr:
        count += getGreedy(i,minVal)     
    return count
    
def getGreedy(i,minVal):
    i = i - minVal
    opers = 0
    opers += i/5 + (i%5)/2 + (i%5)%2
    return opers
    
# Main function for the program
NMinOper = getMinOper([2,2,3,7])
result = NMinOper
print result