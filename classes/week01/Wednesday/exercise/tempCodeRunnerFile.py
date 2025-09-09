myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
length = len(myList)
shifted_list = [None] * length

shift = 3

for idx in range(length):
  new_idx = (idx + 3) % length
  shifted_list[new_idx] = myList[idx]
print(shifted_list)