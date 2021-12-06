'''
class StudentInfo :
    name = " "
    roll = " "
    cgpa = " "
    session = " "

    def __init__(self,name, roll, cgpa, session) :    #This is constructor methode
        self.name = name
        self.roll = roll
        self.cgpa = cgpa
        self.session = session

    def display(self):
        print(f" Name : {self.name}, Roll : {self.roll}, Cgpa : {self.cgpa}, Session : {self.session}")


rahim = StudentInfo("KHalekuzzman","1910979158","3.85","2018-19")
# rahim.setValue("Khalekuzzaman","191","3.95","20")
rahim.display()

karim = StudentInfo("Kaochar","158","3.65","2019-20")
# karim.setValue("kaochar","161","3.85","70")
karim.display()

'''
'''
# Triangle area calculation methode
class Triangle :
    base = " "
    height = " "

    def __init__(self,base,height):
        self.base = base
        self.height = height


    def display(self):
        print(f" Base : {self.base}, Height : {self.height}")

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Triangle area  = ",area)


t1 = Triangle(10,20)
t1.display()
t1.calculate_area()

t2 = Triangle(20,30)
t2.display()
t2.calculate_area()
'''
class Sum :
    num1 = " "
    num2 = " "
    num3 = " "

    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def display(self):
        print(f"Number1 : {self.num1}, Number2 : {self.num2}, Number3 : {self.num3}")

    def calculted_sum(self):
        sum = self.num1 + self.num2 + self.num3
        print("Total sum is : ",sum)


n1 = int(input("Enter your first input : "))
n2 = int(input("Enter your second input : "))
n3 = int(input("Enter your third input : "))

t1 = Sum(n1,n2,n3)
t1.display()
t1.calculted_sum()



