import math
from modules.quickSelect import QuickSelect
from modules.bruteForce import closestPointsBF, distance

'''
Given a space of points determines the 
@param space: the space of points as 2D array

@return the smallest distance of points in 2D space and the 2 points
'''
def ClosestPoints(space):
    length = len(space)
    #brute forces for values small than this
    if length <= 3:
        return closestPointsBF(space)

    #Finding the index of the mid point using quick select
    median = QuickSelect(space, math.floor(len(space)/2))

    #spliting the space into 2 halves seperated by the median
    #running closest points recursively on them
    left = ClosestPoints(space[:median])
    right = ClosestPoints(space[median:])
    
    #Determines which one outputs the lowest distance
    minDistance = minD(left, right)
    
    #finds the smallest across boundary
    #compares it the smallest distance discovered so far
    #returns the smallest
    return closestAcross(space, median, minDistance)

'''
Finds the closest points across the boundary

@param space: the space of points as 2D array
@param median: The index of the median in the space
@param minDistance: The tuple of the minimum distance discovered and

@returns the minDistance out of across boundary and given.
'''
def closestAcross(space, median, minDistance):
    #stores the points on the boundary
    boundary = []

    #extracts all the points on the boundary
    for point in space:
        if space[median][0] - minDistance[0] < point[0] < space[median][0] + minDistance[0]:
            boundary.append(point)

    #Sorts the set by y coordinates
    ySorted = sorted(boundary, key=lambda x: x[1])

    #Compares all the y sorted to the most significant y coordinates
    for i in range(len(ySorted)):
        #Only chooses 6 or number left
        for j in range(1, min(7, len(ySorted) - i)):
            tempDistance = distance(ySorted[i], ySorted[i + j])
            if tempDistance < minDistance[0]:
                minDistance = tempDistance, ySorted[i], ySorted[i + j]

    #returns the true minimum of space
    return minDistance


#Compares which list has a smaller first element
def minD(dl, dr):
    if dl[0] > dr[0]:
        return dr
    else:
        return dl
