#divide list into 2 list, combine 2 sorted lists into 1 sorted list 
from combine import combine as cx
def combine_sort(unsorted):
    size = len(unsorted)

    left = unsorted[0:1]
    for idx in range(1, size):
        #gets a list of size 1 (idx:idx+1)
        right = unsorted[idx:idx+1]
        left = cx(left, right)
    return left

left = combine_sort([5, 4, 3, 2, 1])
print(f'the sorted list is {left}')