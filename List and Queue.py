# List в Python - упорядоченная и изменяемая коллекция элементов.

# Основные свойства:
# 1. Упорядоченность: элементы хранятся в том порядке, в котором они были добавлены.
# 2. Изменяемость: можно добавлять, удалять и изменять элементы после создания списка.
# 3. Индексируемость: к каждому элементу можно обратиться по его позиции (индексу).
# 4. Допускают дубликаты


# Создание List
# Основной синтаксис: элементы заключаются в квадратные скобки и разделяются запятыми
list = []  # Пустой список - O(1)
number = [1, 2, 3, 4, 5]  # Список с числами - O(n)
string = ["a", "abc", "abcd"]  # Список со строками - O(n)
mixed = [2, "python", 4.23, True]  # Список с различными типами данных - O(n)
print("Example of mixed list: ", f"{mixed = }\n")


# Методы
# Покажем на пустом list из примера выше
print("Empty list ->", f"{list = }")

# append(elem) — добавляет элемент в конец списка - O(1) амортизированная сложность
list.append(60)
print("After list.append(60) ->", f"{list = }")

# insert(id, elem) — вставляет элемент на заданную позицию (мы вставим в начало) - O(n)
# Если не писать индекс вставки, то error
list.insert(0, 50)
print("After list.insert(0,50) ->", f"{list = }")

# Добавим еще элементов для наглядности
for i in range(4):
    list.insert(i, 10 + 10 * i)
print("After more inserts ->", f"{list = }")

# reverse() - разворачивает list - O(n)
list.reverse()
print("After reverse ->", f"{list = }")

# index(elem) - возвращает индекс первого вхождения заданного элемента - O(n)
print("Index of '10' is", list.index(10))

# count(elem) - возвращает количество элементов, равных заданному - O(n)
print("Count of '10' is", list.count(10))

# remove(elem) — удаляет первое вхождение элемента из списка - O(n)
list.remove(10)
print("After list.remove(10) ->", f"{list = }")

# pop(id) — удаляет элемент из списка по указанному индексу - O(n) для произвольного индекса
list.pop(0)
print("After list.pop(0) ->", f"{list = }")

# pop() — удаляет последний элемент - O(1)
list.pop()
print("After list.pop() ->", f"{list = }")

# sort() - сортирует list - O(n log n)
list.sort()
print("After list.sort() ->", f"{list = }")

# Если list состоит из строк то сортирует в лексикографическом порядке
# sort поддерживается для строковых списков и не поддерживается для смешанных списков
strings2 = ["python", "hello", "24cst-7"]
print("Strings2 is", f"{strings2 = }")

# clear() - удаляет все элементы списка - O(n)
# copy() - возвращает копию списка - O(n)
list2 = list.copy()
print("List2 is", f"{list2 = }\n")


# Также существуют встроенные функции для работы со списками в Python:
# len(list) — возвращает длину списка - O(1)
print("Длина strings2: ", len(strings2))

# sorted(list) — возвращает отсортированный список - O(n log n)
sorted(strings2)
print("After sorted(strings2) ->", f"{strings2 = }")

# min(list), max(list) — возвращает наименьший/наибольший элемент списка - O(n)
print("Min of list is", min(list))
print("Max of list is", max(list), "\n")


# Операции с list
list = [1, 2, 3.14, 4, 5]
list2 = [6, 7, 8]
print("Список:" f"{list = }")

# Замена значения по индексу - O(1)
list[2] = 3
print("Замена значения: ", f"{list = }")

# Объединение списков (конкатенация) - O(n+m), где n и m - размеры списков
list = list + list2
print("Объединение списков: ", f"{list = }")

# Разложение на переменные (unpacking) - O(n)
a, b, c = list2
print("Разложение на переменные a,b,c:", a, b, c)

# Перебор элементов (итерация) - O(n)
print("Перебор элементов: ")
for num in list:
    print(num)

# Сравнение списков - O(n) в худшем случае
print("List равен list2:", list == list2,"\n\n")


# Queue (Очередь) в Python - структура данных, работающая по принципу FIFO (First In, First Out).

# Основные свойства:
# 1. FIFO: первый добавленный элемент будет первым удален.
# 2. Упорядоченность: элементы извлекаются в том же порядке, в котором добавлялись.
# 3. Ограниченный доступ: элементы добавляются в конец, удаляются из начала.

from collections import deque

# Создание deque (double-ended queue) - двусторонняя очередь
queue = deque()  # Пустая очередь - O(1)
queue_from_list = deque([1, 2, 3, 4])  # Очередь из списка - O(n)
print("Queue from list:", queue_from_list)

# Основные методы для работы с очередью FIFO
print("Empty queue:", queue)

# append(elem) - добавляет элемент в конец очереди - O(1)
queue.append(10)
queue.append(20)
queue.append(30)
print("After adding elements:", queue)

# popleft() - удаляет и возвращает элемент из начала очереди - O(1)
first_item = queue.popleft()
print("First item removed:", first_item)
print("Queue after removing:", queue)

# appendleft(elem) - добавляет элемент в начало очереди - O(1)
queue.appendleft(5)
print("After adding to front:", queue)

# pop() - удаляет и возвращает элемент с конца - O(1)
last_item = queue.pop()
print("Last item removed:", last_item)
print("Queue after removal:", queue)

# Добавим элементы для демонстрации
# extend(iterable) - добавляет элементы в конец - O(k)
queue.extend([40, 50, 60])
print("After extend:", queue)

# count(elem) - подсчитывает количество элементов - O(n)
print("Count of '5':", queue.count(5))

# remove(elem) - удаляет первое вхождение элемента - O(n)
queue.remove(5)
print("After remove(5):", queue)

# reverse() - разворачивает очередь - O(n)
queue.reverse()
print("After reverse:", queue)

# rotate(n) - поворачивает очередь на n позиций - O(k), где k = min(n, len(queue))
queue.rotate(2)
print("After rotate(2):", queue)