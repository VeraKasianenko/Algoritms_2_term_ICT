def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k



things = {'1': [2, 1500], '2': [1, 1000], '3': [4, 5000], '4': [3, 2000], '5': [2, 1250], '6': [3, 2500]}
M = 3 #кол-во заходов
K = 4 #кг
cnt = 0
check_bag = 0
bank = 0
while cnt != M:
    check_bag = 0
    while check_bag < K:
       if max(things.values())[0] + check_bag <= K:
           a = get_key(things, max(things.values()))
           b = things[a]
           check_bag+=b[0]
           bank+=b[1]
           del things[a]
       else:
           break
    cnt+=1
print(f"Вор украл на сумму {bank}")
print('Оптимальный результат: 11250')
#Результат алгоритма: 9500
#лучший вариант: 11250