import math
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
        #Sorting the Space by Y
        space = sorted(space, key=lambda x: x[1])
        return closestPointsBF(space), space

    median = math.floor(len(space)/2)
    #spliting the space into 2 halves seperated by the median
    #running closest points recursively on them
    left = ClosestPoints(space[:median])
    right = ClosestPoints(space[median:])

    #Merge to maintain the y sorted nature
    # ySorted = left[1]
    # i = 0
    # j = 0
    # while j < len(right[1]):
    #     if ySorted[i][1] > right[1][j][1]:
    #         ySorted.insert(i, right[1][j])
    #         j += 1
    #     i += 1
    #     if i == len(ySorted):
    #         for k in range(j, len(right[1])):
    #             ySorted.append(right[1][k])
    #         break
    ySorted = sorted(space, key=lambda x: x[1])
    if sorted(space) != sorted(ySorted):
        print("Aiuto")
    #Determines which one outputs the lowest distance
    minDistance = minD(left[0], right[0])
    #finds the smallest across boundary
    #compares it the smallest distance discovered so far
    #returns the smallest
    return closestAcross(ySorted, space[median], minDistance), ySorted


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
        if median[0] - minDistance[0] < point[0] < median[0] + minDistance[0]:
            boundary.append(point)
    #Compares all the y sorted to the most significant y coordinates
    for i in range(len(boundary)):
        #Only chooses 6 or number left
        for j in range(1, min(7, len(boundary) - i)):
            tempDistance = distance(boundary[i], boundary[i + j])
            if tempDistance < minDistance[0]:
                minDistance = tempDistance, boundary[i], boundary[i + j]

    #returns the true minimum of space
    return minDistance


#Compares which list has a smaller first element
def minD(dl, dr):
    if dl[0] > dr[0]:
        return dr
    else:
        return dl
