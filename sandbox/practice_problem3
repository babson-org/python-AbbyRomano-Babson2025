#count number of even numbers in a list

def count_evens(nums):
    #create base case for empty list
    if len(nums) == 0:
        return 0
    #first element of list at index 0 is stored in first variable
    first = nums[0]
    #take everything but num at index 0 and store in variable called rest
    rest = nums[1:]

    if first % 2 == 0:
        #return 1 plus the rest of the evens in the list to be counted
        return 1 + count_evens(rest)
    else:
        return count_evens(rest)
    
print(count_evens([2, 1, 2, 3, 4]))  # Should print 3