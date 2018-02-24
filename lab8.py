#1 Cчитывание с файла, работа с буквами
def longest_sequence(s):
    l = 0
    max = 0
    for i in range(len(s)):
        if s[i] == 'а':
            l += 1
        else:
            if l > max:
                max = l
            l = 0
    if l > max:
        max = l
    return max
f = open('test1.txt','r',encoding='cp1251')
s = f.read()
f.close()
print("1)Самая длинная последовательность: ",longest_sequence(s))
print (s)
#2 Считывание с файла, работа с большими списками.
def count_high(s):
    count = 0
    for i in range (len(s)):
        if i%2 != 0:
            f = 1
            x = s[i]
            for j in range (len(x)):
                if(x[j] != '5'):
                    f = 0
                    break
            if(f == 1):
                count += 1
    return count
f = open('test2.txt','r',encoding='cp1251')
s = f.read().split()
f.close()
print("2)Число отличников: ",count_high(s))
print(s)
#3 Запись в файл.
def read_file(s):
    a = []
    x = ''
    for i in range(len(s)):
        x += s[i]
        if(s[i] == '\n'):
            a += [x]
            x = ''
    a += [x]
    return a
def write_file(a):
    s = ''
    for i in range(len(a)):
        s += a[i]
    return s
#1 действие
f1 = open('1.txt','r')#откроем первый файл
s = f1.read()
f1.close()
a = read_file(s)
f3 = open('3.txt','w')#запишем первый в третий
f3.write(write_file(a))
f3.close()
#2 действие
f2 = open('2.txt','r')#откроем второй для чтения
s = f2.read()
f2.close()
a = read_file(s)
f1 = open('1.txt','w')#запишем в первый из второго
f1.write(write_file(a))
f1.close()
#3 действие
f3 = open('3.txt','r')#откроем третий для чтения
s = f3.read()
f3.close()
a = read_file(s)
f2 = open('2.txt','w')#запишем во второй из третьего
f2.write(write_file(a))
f2.close()





