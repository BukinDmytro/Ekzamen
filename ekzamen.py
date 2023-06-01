#9
l2=[]
def f(l):
    l1 = l.split(" ")
    for i in l1:
        if "Pyton" in i:
            l2.append(i)
l = input("введіть слова через пробіл")
f(l)
print(f"Cисок зі слві pyton"