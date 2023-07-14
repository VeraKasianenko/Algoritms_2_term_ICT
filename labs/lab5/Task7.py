nums = [int(i) for i in input("Введите числа: ").split()]
minn = min(nums)
maxx = max(nums)

hashset = set()
for i in nums:
    hashset.add(i)

for i in range(minn, maxx + 1):
    if not(i in hashset):
        print(f"Минимальное пропущенное число: {i}")
        break
