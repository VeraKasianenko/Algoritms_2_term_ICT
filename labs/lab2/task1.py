import random

a = input('Введите строку ')
arr = []
for i in range(len(a)):
    arr.append(ord(a[i]))


hash = []
C = random.uniform(0, 1)
for i in range(len(arr)):
    Key = arr[i]
    M = len(arr)
    res = round(M*((Key*C)%1))
    hash.append(str(res))

print(''.join(hash))
