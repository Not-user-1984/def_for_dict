# Примеры использования циклов в Python

# 1. Цикл for: Перебор списка
print("=== Пример 1: Перебор списка ===")
fruits = ["яблоко", "банан", "груша"]
for fruit in fruits:
    print(fruit)

# 2. Цикл for с range
print("\n=== Пример 2: Использование range ===")
for i in range(5):  # Перебирает числа от 0 до 4
    print(i)

# # 3. Перебор словаря
# print("\n=== Пример 3: Перебор словаря ===")
# person = {"имя": "Алексей", "возраст": 25}
# for key, value in person.items():
#     print(f"{key}: {value}")

# 4. Цикл for с шагом в range
print("\n=== Пример 4: Чётные числа с range ===")
for i in range(0, 10, 2):  # Чётные числа от 0 до 8
    print(i)

# 5. Цикл while: Простой счётчик
print("\n=== Пример 5: Простой счётчик в while ===")
count = 0
while count < 5:
    print(count)
    count += 1

# 6. Цикл while с вводом пользователя (комментируем, чтобы не блокировать выполнение)
print("\n=== Пример 6: Цикл while с вводом пользователя ===")
user_input = ""
while user_input != "выход":
    user_input = input("Введите что-нибудь (или 'выход' для завершения): ")
    print(f"Вы ввели: {user_input}")

# 7. Цикл while с break
print("\n=== Пример 7: Бесконечный цикл с break ===")
counter = 0
while True:
    print(f"Счётчик: {counter}")
    counter += 1
    if counter >= 3:
        break  # Выход после 3 итераций

# 8. Использование break в цикле for
print("\n=== Пример 8: Использование break в for ===")
for i in range(10):
    if i == 5:
        break  # Прерывает цикл, когда i равно 5
    print(i)

# 9. Использование continue в цикле for
print("\n=== Пример 9: Использование continue в for ===")
for i in range(5):
    if i == 2:
        continue  # Пропускает i=2
    print(i)

# 10. Цикл for с else
print("\n=== Пример 10: Цикл for с else ===")
for i in range(5):
    print(i)
else:
    print("Цикл завершён!")

# 11. Цикл for с break и else (else не выполнится)
print("\n=== Пример 11: Цикл for с break и else ===")
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Этот текст не выведется из-за break")

# 12. Вложенные циклы: Таблица умножения
print("\n=== Пример 12: Вложенные циклы (таблица умножения) ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")

# 13. Функция с циклом for: Сумма элементов списка
print("\n=== Пример 13: Функция с циклом for ===")


def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_list([1, 2, 3, 4]))  # Вывод: 10

# 14. Функция с циклом while: Сумма элементов списка
print("\n=== Пример 14: Функция с циклом while ===")


def sum_while(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total


print(sum_while([1, 2, 3, 4]))  # Вывод: 10

# 15. Генератор списка вместо цикла
print("\n=== Пример 15: Генератор списка вместо цикла ===")
squares = [i * i for i in range(5)]
print(squares)  # Вывод: [0, 1, 4, 9, 16]
