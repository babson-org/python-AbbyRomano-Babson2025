
numbers = []
for i in range(5):
    num = int(input(f'enter number {i+1}: '))
    numbers.append(num)
total = sum(numbers)
average = total / len(numbers)
print('numbers', numbers)
print('total', total)
print('average', average)