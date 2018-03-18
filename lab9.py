#1)	Отсортировать в матрице столбцы по убыванию значений элементов в первой строке
import random
n = 10
a = []
print("1)Отсортировать в матрице столбцы по убыванию значений элементов в первой строке:")
for i in range(n):
    a.append([])
    for j in range(n):
        a[i] += [random.randint(1,100)]
print(a)
i = 0
while i < n:
    j = 0
    while j < n - 1:
        if (a[0][j] > a[0][j + 1]):
            for k in range (n):
                a[k][j],a[k][j + 1]=a[k][j + 1],a[k][j]
        j += 1
    i += 1
print (a,"\n")
#2)	Последний отрицательный элемент каждого столбца двумерного массива заменить нулём.
n = 3
a = []
print("2)Последний отрицательный элемент каждого столбца двумерного массива заменить нулём:")
for i in range(n):
    a.append([])
    for j in range(n):
        a[i] += [random.randint(-100,100)]
print(a)
j = 0
while j < n:
    i = 0
    li = -1
    lj = -1
    while i < n:
        if(a[i][j] < 0):
            li = i
            lj = j
        i += 1
    if(li != -1 and lj != -1):
        a[li][lj] = 0
    j += 1
print(a,"\n")
#3)	Определить среднее число студентов в одной группе на третьем курсе.
c = 5
g = 8
a = []
print("3)Определить среднее число студентов в одной группе на третьем курсе:")
for i in range(g):
    a.append([])
    for j in range(c):
        a[i] += [random.randint(5,30)]
print(a)
group = 2
sum = 0
for j in range(len(a[group])):
    sum += a[group][j]
print (sum/len(a[group]),"\n")
#4)Изменить массив так, чтобы в нем не было результатов пятого этапа,
# отсортировать массив и определить первые три места.
r = 16
t = 12
a = []
print("4)Удалить пятый этап и определить первые три места:")
for i in range(r):
    a.append([])
    for j in range(t):
        a[i] += [round(random.uniform(10,20),2)]
print(a,"\n")
drop = 5 #удаляем пятый этап
for i in range(len(a)):
    a[i] = a[i][:drop - 1] + a[i][drop:]
print (a,"\n")
result = []
for i in range(r):
    temp = 0
    result.append([])
    for j in range(t - 1):
        temp += a[i][j]
    result[i] += [round(temp,2)]
    result[i] += [i + 1]
result.sort()
print (result[15],result[14],result[13])



