def count(n):
    if (n - 1 == 0):
        return 1
    elif (n - 2 == 0):
        return 2
    elif (n - 3 == 0):
        return 4
    else:
        return count(n - 1) + count(n - 2) + count(n - 3)


n = int(input("Введите кол-во ступенек: "))
print(f"Кол-во путей: {count(n)}")

