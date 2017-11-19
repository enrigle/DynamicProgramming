"""
All the children sit in a line (their positions are fixed), and each  of them 
has a rating score according to his or her performance in the class.  Alice wants 
to give at least 1 candy to each child. If two children sit next to each other, 
then the one with the higher rating must get more candies. Alice wants to save 
money, so she needs to minimize the total number of candies given to the children.
"""
def candies(n, ratings):
    "n, array -> int"
    "purpose: minimize number of candies given to childen"
    #constrains: to give at least 1 candy to each child
    #If 2 children sit next to each other, then the one with 
    #the higher rating must get more candies
    candies = [1 for x in range(n)]
    #increase count on the right of local minimas
    #transient nodes (S) R(S+1) > R(S) get updated
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    #increase count on the left of local minimas
    #transient nodes (S) R(S) > R(S+1) gets updated
    #local maximas should be max of left and right                        
    for i in range(n-2, 0, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
                
    #get the sum
    return sum(candies)
    
print candies(3, [1, 2, 2]) #2. 1, 2, 1 
print candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]) #19. 1, 2, 1, 2, 1, 2, 3, 4, 2, 1
