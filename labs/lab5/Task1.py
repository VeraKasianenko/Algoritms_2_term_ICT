nums = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    nums[i][0], nums[i][1], nums[i][2] = input(f"Введите {i+1} строку: ").split()

flag = 0
for i in range(3):
    if (nums[i][0] == nums[i][1] == nums[i][2] == "x"):
        flag = 1
    if (nums[0][i] == nums[1][i] == nums[i][2] == "x"):
        flag = 1
if (nums[0][0] == nums[1][1] == nums[2][2] == 'x'):
    flag = 1
if (nums[0][2] == nums[1][1] == nums[2][0] == 'x'):
    flag = 1
for i in range(3):
    if (nums[i][0] == nums[i][1] == nums[i][2] == "o"):
        flag = 2
    if (nums[0][i] == nums[1][i] == nums[2][i] == "o"):
        flag = 2
if (nums[0][0] == nums[1][1] == nums[2][2] == 'o'):
    flag = 2
if (nums[0][2] == nums[1][1] == nums[2][0] == 'o'):
    flag = 2

if (flag == 1):
    print("Победили крестики!")
elif (flag == 2):
    print("Победили нолики!")
else:
    print("Ничья!")





