left = [1, 7, 27, 36]
right = [3, 6, 15, 39]

def combine(left, right):
    array = [ ]
    left_current = 0
    right_current = 0

    while left_current < len(left) and right_current < len(right):
        if left[left_current] < right[right_current]:
            array.append(left[left_current])
            left_current += 1
        else:
            array.append(right[right_current])
            right_current += 1
    
    while left_current < len(left):
        array.append(left[left_current])
        left_current += 1
    
    while right_current < len(right):
        array.append(right[right_current])
        right_current += 1

    return array

print(combine(left, right))