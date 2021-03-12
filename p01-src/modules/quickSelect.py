import math

'''
@param items the array to find kth index of
@param item_index the kth index to find 
'''
def QuickSelect(items, item_index):

    # Checks if the is list has items in it
    if items is None or len(items) < 1:
        return None
    # Checks the Index is not greater than the length of the list
    if item_index < 0 or item_index > len(items) - 1:
        raise IndexError()
    #Runs the quick select algorithm
    return select(items, 0, len(items) - 1, item_index)


'''
@param lst the list being partitioned
@param l the begining index of the left side
@param r the begining index of the right side
@param index the k-th biggest index we are looking for
'''
def select(lst, l, r, index):
    # base case
    if r == l:
        return r

    # choose random pivot
    pivot_index = choosePivot(lst[l:r+1]) + l
    # move pivot to beginning of list
    lst[l], lst[pivot_index] = lst[pivot_index], lst[l]
    # partition
    # Last available Space
    i = l
    for j in range(l+1, r+1):
        if lst[j] < lst[i]:
            if j > i + 1:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            lst[j], lst[i] = lst[i], lst[j]
            i += 1

    # recursively partition one side only
    if index == i:
        return i
    elif index < i:
        return select(lst, l, i-1, index)
    else:
        return select(lst, i+1, r, index)

# Avoid worse cases of sorted array.
# Reproducable unlike using random index to get result.
def choosePivot(collection):
    return math.floor(len(collection)/2)

