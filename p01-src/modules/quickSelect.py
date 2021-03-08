import math

'''
@param items the array to find kth index of
@param item_index the kth index to find 
'''
def QuickSelect(items, item_index):

    if items is None or len(items) < 1:
        return None
    if item_index < 0 or item_index > len(items) - 1:
        raise IndexError()
    return select(items, 0, len(items) - 1, item_index)

def select(lst, l, r, index):
    # print("*** ", lst[l:r+1], " ***")
    # base case
    if r == l:
        # print(lst[l:r+1])
        return r

    # choose random pivot
    pivot_index = choosePivot(lst[l:r+1]) + l
    # move pivot to beginning of list
    lst[l], lst[pivot_index] = lst[pivot_index], lst[l]
    # partition
    # Last available Space
    i = l
    # print("Pivot: ", lst[l])
    for j in range(l+1, r+1):
        if lst[j] < lst[i]:
            # print("j: ", lst[j], " i: ", lst[i])
            # print("First: ", lst[l:r + 1])
            if j > i + 1:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            # print("Second: ", lst[l:r + 1])
            lst[j], lst[i] = lst[i], lst[j]
            # print("Third: ", lst[l:r+1])
            # print("Changes: ", lst)
            i += 1

    # recursively partition one side only
    if index == i:
        # print(i)
        # print("index: ", i)
        # print("index value: ", lst[i])
        return i
    elif index < i:
        return select(lst, l, i-1, index)
    else:
        return select(lst, i+1, r, index)
#Avoid worse cases of sorted array.
#Reproducable unlike using random index to get result.
def choosePivot(collection):
    return math.floor(len(collection)/2)

