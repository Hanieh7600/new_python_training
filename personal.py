import jdatetime

class Personal:
    def __init__(self , firstname,lastname,birthday,mobile,sex):
        self.firstname=firstname
        self.lastname=lastname
        self.mobile=mobile
        self.birthday=birthday
        self.sex=sex
        self.date_birth = 0
        self.month_birth =0
        self.year_birth = 0
        self.Age()



    def Age(self):
        age=self.birthday.split("/")
        day_birthday = int(age[2])
        month_birthday = int(age[1])
        year_birthday = int(age[0])

        day_today = int(jdatetime.datetime.now().strftime("%d"))
        month_today = int(jdatetime.datetime.now().strftime("%m"))
        year_today = int(jdatetime.datetime.now().strftime("%Y"))

        month = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]

        if month_birthday > month_today:
            year_today = year_today - 1
            month_today = month_today + 12

        if day_birthday > day_today:
            day_today = day_today + month[month_birthday - 1]
            month_today = month_birthday - 1

        self.date_birth = day_today - day_birthday
        self.month_birth = month_today - month_birthday
        self.year_birth = year_today - year_birthday

    def Print(self):
        month = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
        if self.sex=='zan':
            print(" miss "+self.firstname+' '+self.lastname)
        elif self.sex=='mr':
            print("mr"+self.firstname+' '+self.lastname)
        else:
            print( self.firstname + ' ' + self.lastname)

        print('mobile:'+self.mobile)
        print('birthday:'+self.birthday)

        print(str(self.year_birth)+'year - ' +str(self.month_birth)+'month  - '+str(self.date_birth)+'days ')

        days =0
        for i in range(self.month_birth+1):
            days+=month[i]

        print(self.year_birth*365 + self.date_birth + days )



p=Personal(input('please enter firstname:'),input('please enter lastname:'),input('please enter birthday:'),input('please enter mobile:'),input('please enter Gender:'))
print(p.Print())

