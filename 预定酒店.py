import random

n = 10
k = 3
x = 100
arr = [80, 90, 100, 110, 120]
arr = []
for i in range(n):
    arr.append(random.randint(0, 200))

result = arr[:k]
result.sort()
print(arr)

for index in range(k, n):
    current = arr[index]
    first = result[0]
    last = result[k-1]
    dLast = abs(last-x)
    dFirst = abs(first-x)
    if dLast >= dFirst:
        if abs(current-x) < dLast:
            result.pop()
            result.append(current)
            result.sort()
    else:
        if abs(current-x) < dFirst:
            result.pop(0)
            result.append(current)
            result.sort()
print(result)
