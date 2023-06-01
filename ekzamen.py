def strings(strings):
    b = []
    for string in strings:
        if string[0].isupper():
            b.append(string)
    return b
a = input("Введіть список рядків, розділениx прробідами: ").split(" ")
result = strings(a)
print("Результат:", result)
