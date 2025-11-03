list = [3, 5, 6, 2, 8, 1, 4, 7]
def bubble_sort(list):
    num_items = len(list)
    #loops through for each item in list (through entire index)
    for i in range(num_items):
        #for each item in the list, if the right is larger than left, swap otherwise do nothing 
        for j in range(0, num_items-i-1):
            if list[j] > list[j +1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
print(bubble_sort(list))


#SIMPLY
def bubble_sort_simple(values):
    sorted = values.copy()
    size = len(sorted)

    for pass_num in range(size - 1):
        for idx in range(size - 1 - pass_num):
            if sorted[idx] > sorted[idx + 1]:
                sorted[idx], sorted[idx + 1] = sorted[idx + 1], sorted[idx]
    return sorted
print(bubble_sort_simple([3, 5, 6, 2, 8, 1, 4, 7]))
