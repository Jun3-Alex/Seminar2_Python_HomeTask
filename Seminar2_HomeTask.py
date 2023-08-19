# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
'''
n = int(input(f"Введите число монет: "))

coins = input(f"Введите последовательность монет(O - орел,R - решка): ")

orel_count = 0
reshka_count = 0

for coin in coins:
    if coin == 'O':
        orel_count +=1
    elif coin == 'R':
        reshka_count +=1

if orel_count < reshka_count:
    min_flips = orel_count
else:
    min_flips = reshka_count    

print(f"Минимальное количество переворотов:{min_flips}")            

'''

# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
S = int(input(f"Введите сумму чисел: "))
P = int(input(f"Введите произведение чисел: "))

X = 1
Y = P

while X <= Y:
    if X * Y == P and X + Y == S:
        break
    X += 1
    Y = P // X
if X <= Y:
    print(f"Число {X}, Число {Y}")
else:
    print(f"Нет подходящих значений X и Y")    

'''







