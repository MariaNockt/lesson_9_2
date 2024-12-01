first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Список длин строк из first_strings, длина которых не менее 5 символов
first_result = [len(f) for f in first_strings if len(f) >= 5]

# Список пар слов (кортежей) одинаковой длины
second_result = [(s, f) for s in first_strings for f in second_strings if len(f) == len(s)]

# Словарь, где ключ - строка, значение - длина строки, только для строк с чётной длиной
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Результаты
print(first_result)
print(second_result)
print(third_result)