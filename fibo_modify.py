# import sys
# 
# t1, t2, n = raw_input().strip().split(' ')
# t1, t2, n = [int(t1), int(t2), int(n)]
# print t1, t2, n

def f(a, b, n):
    for i in range(0, n-1):
        a, b = b, a + b**2
    return a
    
print f(0, 1, 10)