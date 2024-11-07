first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Список длин строк из first_strings, где длина строк не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Список кортежей, содержащих пары слов одинаковой длины
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# Словарь, где ключ - строка, значение - длина строки (чётная длина)
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

print(first_result)  # Вывод: [10, 8, 8]
print(second_result)  # Вывод: [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
print(third_result)  # Вывод: {'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Computer': 8}

