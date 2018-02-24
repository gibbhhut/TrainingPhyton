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
    s = s[0:-1]#остальная строка
    s = s.replace(p,'')
    a[i] = s + p
print (a)
print("\n")
#3
print("3)Введите слова через пробел")
a = input().split()
for i in range(len(a)):
    a[i] = a[i].replace('жы','жИ')
    a[i] = a[i].replace('шы','шИ')
    a[i] = a[i].replace('чя','чА')
    a[i] = a[i].replace('щя','щА')
    a[i] = a[i].replace('чю','чУ')
    a[i] = a[i].replace('щю','щУ')
print (a)
print("\n")
#4
print("4)Введите слова через пробел")
a = input().split()
b = []
f1 = 0
f2 = 0
for i in range(len(a)):
    f1 = 0
    f2 = 0
    j = 0
    #повторяется ли текущее слово в заданной
    #последовательности
    while j < len(a):
        if(a[i] == a[j] and i != j):
            f1 = 1
            break
        j += 1
    #если слово встретилось только один раз
    #проверим записано ли оно уже в выходной
    #массив b
    if(f1 == 0):
        for j in range(len(b)):
            if(a[i] == b[j]):
                f2 = 1
                break
        if(f2 == 0):
            b.append(a[i])
print (b)
