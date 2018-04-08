class Time:

    def __init__(self,time,hour = '',minute = '',second = '', validation = True):
        time = time.split(":")
        if(int(time[0])>=0 and int(time[0])<=24)and(int(time[1])>=0 and int(time[1])<=59)and(int(time[2])>=0 and int(time[2])<=59):
            self.validation = True
        else:
            self.validation = False
        self.hour = time[0]
        self.minute = time[1]
        self.second = time[2]
    def __str__(self):
        if(self.validation == True):
            return self.hour+":"+self.minute+":"+self.second
        else:
            return "Errors!"
    def into_second(self):
        return int(self.hour)*60*60 + int(self.minute)*60 + int(self.second)
    def from_second(self,temp):
        self.hour = str(temp//3600)
        temp = temp%3600
        self.minute = str(temp//60)
        temp = temp%60
        self.second = str(temp)
    def add(self,time):
        time = Time(time)
        if(time.validation == True):
            temp1 = self.into_second()
            temp2 = time.into_second()
            temp1 = temp1 + temp2
            self = self.from_second(temp1)
    def compare(self,a):
        time = a[0].into_second()
        max = time;index = 0
        for i in range(len(a)):
            time = a[i].into_second()
            a[i] = time
            if a[i]>max:max=a[i];index=i
        return self.from_second(a[index])


value1 = Time("10:10:15")
print(value1)
value2 = Time("5:10:15")
print(value2)
array = [value1,value2]
value1.compare(array)
print("Наибольшее время:",value1)
