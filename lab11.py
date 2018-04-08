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
    def add(self,time):
        time = Time(time)
        if(time.validation == True):
            temp1 = int(self.hour)*60*60 + int(self.minute)*60 + int(self.second)
            temp2 = int(time.hour)*60*60 + int(time.minute)*60 + int(time.second)
            temp1 = temp1 + temp2
            self.hour = str(temp1//3600)
            temp1 = temp1%3600
            self.minute = str(temp1//60)
            temp1 = temp1%60
            self.second = str(temp1)

value1 = Time("10:20:30")
print(value1)
value1.add("5:10:15")
print(value1)
