#1
print("1)Введите слова через пробел")
a = input().split()
for i in range(len(a)):
    j = 0
    while j + 1 < len(a):
        if(a[j] > a[j + 1]):
            a[j],a[j + 1] = a[j + 1],a[j]
        j += 1
print (a)
print("\n")
#2
print("2)Введите слова через пробел")
a = input().split()
for i in range(len(a)):
    s = a[i]
    p = s[len(s) - 1]#последний элемент
    s = s.replace(p,'')
    a[i] = s + p
print (a)
print("\n")
#3
print("3)Введите слова через пробел")
a = input().split()
d = {'жы': 'жИ', 'шы': 'шИ','чя':'чА','щя':'щА'}
for i in range(len(a)):
    a[i] = a[i].replace(d,'жИ')
print (a)
print("\n")
#4
print("4)Введите слова через пробел")
a = input().split()
b = []
f = 0
for i in range(len(a)):
    f = 0
    j = 0
    #повторяется ли текущее слово в заданной
    #последовательности
    while j < len(a):
        if(a[i] == a[j] and i != j):
            f = 1
            break
        j += 1
    if(f == 0):
        b.append(a[i])
print (b)
