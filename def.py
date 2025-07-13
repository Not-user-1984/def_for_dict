def add_numbers(a, b):
    result = a + b
    return result


# Вызов функции
sum = add_numbers(4, 4)
print(sum)


# Параметры: Могут быть обязательными, необязательными (с значениями по умолчанию),
def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"


# Документация: Можно добавлять строку документации (docstring) для описания функции:
print(greet("Алексей"))  # Вывод: Привет, Алексей!
print(greet("Алексей", greeting="Здравствуй"))  # Вывод: Здравствуй, Алексей!


def multiply(a, b):
    """Умножает два числа и возвращает результат."""
    return a * b


print(multiply.__doc__)


# Анонимные функции (lambda)

square = lambda x: x * x

print(square(4))  # Вывод: 16


def apply_function_to_list(func, data):
    """Применяет функцию func к каждому элементу списка data."""
    return [func(item) for item in data]


# Определяем функции, которые будем передавать
def square(x):
    return x * x


def double(x):
    return x * 2


# Список чисел
numbers = [1, 2, 3, 4]

# Передаём функцию square
result1 = apply_function_to_list(square, numbers)
print(result1)  # Вывод: [1, 4, 9, 16]

# Передаём функцию double
result2 = apply_function_to_list(double, numbers)
print(result2)  # Вывод: [2, 4, 6, 8]
