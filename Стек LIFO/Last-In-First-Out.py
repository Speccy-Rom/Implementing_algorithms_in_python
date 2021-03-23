from collections import deque

data = deque()
data.append('Красный')
data.append('Синий')
data.append('Черный')
data.append('Белый')

print(data)

deque(['Красный', 'Синий', 'Черный', 'Белый'])

last = data.pop()
print(last)

print(data)

deque(['Красный', 'Синий', 'Черный'])