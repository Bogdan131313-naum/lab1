items = [12, 3, 25, 8, 42, 7, 19, 6, 4, 15,
         "apple", "banana", "cherry", "grape", "kiwi",
         "pear", "orange", "melon", "fig", "date"]

ints = [x for x in items if isinstance(x, int)]
strings = [x for x in items if isinstance(x, str)]

sorted_list = sorted(ints) + sorted(strings)

even_numbers = [x for x in ints if x % 2 == 0]

strings_caps = [s.upper() for s in strings]

print("Відсортований список:", sorted_list)
print("Кратні двом:", even_numbers)
print("Рядки капсом:", strings_caps)
