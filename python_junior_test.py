import random

# Есть список input_list (python list) целых чисел длинной N. Необходимо выбрать k случайных элементов без повторений по
# индексу . Алгоритм решения должен быть оптимальным по сложности и по ресурсам, определить сложность в нотации O(N,k)
#
# Переводить список в другие структуры данных нельзя. Для получения единичного случайного числа можно использовать метод
# random.randint(A, B). Иные методы из random и в целом сторонние библиотеки использовать нельзя
#
# PS. Пожелание: не забудьте рассмотреть случай k —> N
#
# Пример:
#
# input_list = [1, 3, 4, 3, 3, 9]
#
# k = 3
#
# варианты ответа: [3, 4, 3] или [4, 1, 9] или [3, 1, 4] неправильные вариант ответа: [4, 4, 3] - 4 не должен быть более
# одного раза, потому что во входном списке встречается только единожды


INPUT_LIST = [1, 3, 4, 3, 3, 9, 7, 12, 2, 1]
K = random.randint(1, len(INPUT_LIST))

INDEX_USED = []
RESULT = []

while K > 0:
    num = random.randint(0, len(INPUT_LIST) - 1)

    if num in INDEX_USED:
        continue
    else:
        INDEX_USED.append(num)
        RESULT.append(INPUT_LIST[num])
        K -= 1

# print(RESULT)

# Дополнительно: Решить предыдущую задачу с условием того, что для каждого элемента входного списка есть соответствующая
# вероятность его выпадения. Вероятности представлены отдельным список той же длины. Пример списка вероятностей
# prob = [.7, .4, .5, .9, .1], элементы лежать в диапазоне [0, 1], значения кратны 0.1

INPUT_LIST = [1, 2, 3, 4, 5, 6]  # 1, 3, 4, 3, 3, 9
K = 3  # random.randint(1, len(INPUT_LIST))

CHANCE_LIST = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
INPUT_CHANCE_LIST = []

for i in range(len(INPUT_LIST)):
    chance_num_int = int(CHANCE_LIST[i] * 10)
    chance_num = CHANCE_LIST[i]
    INPUT_CHANCE_LIST.extend([chance_num] * chance_num_int)

INDEX_USED = []
RESULT = []

while K > 0:
    chance = random.randint(1, len(INPUT_CHANCE_LIST) - 1)
    chance_num = INPUT_CHANCE_LIST[chance]
    num = CHANCE_LIST.index(chance_num)

    if num in INDEX_USED:
        continue
    else:
        INDEX_USED.append(num)
        RESULT.append(INPUT_LIST[num])
        K -= 1

print(RESULT)

# gg