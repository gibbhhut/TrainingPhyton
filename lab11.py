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
        if((temp//3600)<10):
            self.hour = "0" + str((temp//3600))
        elif((temp//3600)>=10 and (temp//3600)<=23):
            self.hour = str(temp//3600)
        elif((temp//3600)>23):
            if((temp//3600)%12 < 10):
                self.hour = "0" + str((temp//3600)%12)
            else:
                self.hour = str((temp//3600)%12)
        temp = temp%3600
        if((temp//60)<10):
            self.minute = "0" + str(temp//60)
        else:
            self.minute = str(temp//60)
        temp = temp%60
        if(temp<10):
            self.second = "0" + str(temp)
        else:
            self.second = str(temp)
    def add(self,time):
        time = Time(time)
        if(time.validation == True):
            temp1 = self.into_second()
            temp2 = time.into_second()
            temp1 = temp1 + temp2
            self = self.from_second(temp1)
    def sub(self,time):
        time = Time(time)
        if(time.validation == True):
            temp1 = self.into_second()
            temp2 = time.into_second()
            temp1 = abs(temp1 - temp2)
            self = self.from_second(temp1)
    def compare(self,a):
        time = Time(array[0])
        time = time.into_second()
        max = time;index = 0
        for i in range(len(a)):
            time = Time(array[i])
            time = time.into_second()
            a[i] = time
            if a[i]>max:max=a[i];index=i
        return self.from_second(a[index])
#1)
value1 = Time("12:00:00")
print(value1)
#2)
value1.add("23:00:00")
print(value1)
#3)
array = ["05:05:05","10:10:10","14:08:05"]
value = Time(array[0])
value.compare(array)
print("Наибольшее время:",value)
#4)
value1.sub("23:00:00")
print(value1)
