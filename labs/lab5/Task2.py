def search(nums, k):
    i = 0
    j = m - 1
    while (i <= n) and (j >= 0):
        if (nums[i][j] == k):
            return (i + 1, j + 1)
        if (nums[i][j] > k):
            j -= 1
        else:
            i += 1
    return "Числа нет в матрице"


n = int(input("Введите кол-во строк: "))
m = int(input("Введите кол-во столбцов: "))

nums = []

for i in range(n):
    nums.append([])
    for j in range(m):
        nums[i].append(int(input("Введите элемент: ")))

k = int(input("Введите число, которое нужно найти: "))

print(search(nums, k))





