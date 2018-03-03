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
def open_stream(text,code,action,value,flag):
    f = open(text,action,encoding = code)
    if(action == 'r'):
        s = f.read()
        f.close()
        if(flag == 0):
            a = read_file(s)
            return a
        else:
            return s
    if(action == 'w'):
        f.write(write_file(value))
        f.close()
        return
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
#1 Cчитывание с файла, работа с буквами
s = open_stream('test2.txt','ansi','r',0,1)
print("1)Самая длинная последовательность: ",longest_sequence(s))
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
s = open_stream('test2.txt','cp1251','r',0,1)
s = s.split()
print("2)Число отличников: ",count_high(s))
print(s)
#3 Запись в файл.
#1 действие
a1 = open_stream('1.txt','ansi','r',0,0)#откроем первый файл
open_stream('3.txt','ansi','w',a1,0)#запишем первый в третий
#2 действие
a2 = open_stream('2.txt','ansi','r',0,0)#откроем второй для чтения
open_stream('1.txt','ansi','w',a2,0)#запишем в первый из второго
#3 действие
a3 = open_stream('3.txt','ansi','r',0,0)#откроем третий для чтения
open_stream('2.txt','ansi','w',a3,0)#запишем во второй из третьего
