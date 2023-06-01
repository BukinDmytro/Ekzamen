#5

a = input("введіть слово паліндром якщо хочете ")
reverse = a[::-1]
def palindrom(a):
    while True:
        if a[::1] == reverse:
            print(a, "слово є паліндромом")
            break
        if  a != reverse:
            print(a, "слово не є паліндромом")
            continue
print(palindrom(a))
