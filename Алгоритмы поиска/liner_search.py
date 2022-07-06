from datetime import datetime


def liner_search(lst, x):
    length = len(lst)
    return next((i for i in range(length) if lst[i] == x), None)


items = [2, 3, 5, 7, 11, 13, 17]
print(liner_search(items, 1))  # None
print(liner_search(items, 7))  # 3
print(liner_search(items, 19))  # None

# *** simplified speed test ***
items = range(1000000)
count = 100

start = datetime.now()

for _ in range(1, count):
    liner_search(items, 777777)

delta = datetime.now() - start
totalMicroseconds = delta.seconds * 1000000 + delta.microseconds

print(totalMicroseconds / count)
# about 317368.22 microseconds
