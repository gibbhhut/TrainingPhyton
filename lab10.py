import random
#1. Составить процедуру (функцию), определяющую, в каком из данных двух чисел больше цифр
def countDigit(number):
    count = 0
    if(number == 0):
        return count
    else:
        while number > 0:
            number = number//10
            count += 1
    return count
if(countDigit(0) > countDigit(12)):
    print ("В первом больше")
else:
    print ("Во втором больше")
#2. Вывести на печать матрицу с наименьшей нормой.
def fill_matrix(x,y,n):
    matrix = [[random.randint(x,y) for i in range(n)] for i in range(n)]
    return matrix
def max_abs(matrix):
    max = abs(matrix[0][0])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(max < abs(matrix[i][j])):
                max = abs(matrix[i][j])
    return max
A = fill_matrix(-100,100,3)
B = fill_matrix(-100,100,3)
C = fill_matrix(-100,100,3)
max1,max2,max3 = max_abs(A),max_abs(B),max_abs(C)
print("Матрица с наименьшей нормой: ",max(max1,max2,max3))
#3. Описать функцию С(m,n), для вычисления биномиального коэффициента
def binom(m, n):
    if (0 < m < n):
        return binom(m, n - 1) + binom(m - 1, n - 1)
    else:
        return 1
C = binom(5, 7)
print (C)
#4.	Составить программу нахождения числа, которое образуется из данного натурального числа
#   при записи его цифр в обратном порядке, используя рекурсивную подпрограмму.
def reverse(x,y):
    if(x > 0):
        temp = x%10
        x //= 10
        return reverse(x,temp + y*10)
    else:
        return y + ((x%10))
temp = reverse(1468,0)
print (temp)
