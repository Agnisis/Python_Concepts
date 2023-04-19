class student:
    def __init__(self, name='.', marks=0):
        self.name = name
        self.marks = marks

    def display(self):
        print("name is ", self.name)
        print("marks is ", self.marks)

    def calculate(self):
        if(marks >= 600):
            print("first")
        elif(marks >= 500):
            print("second")
        elif(marks >= 350):
            print("third")
        else:
            print("fail")

n = int(input("how many nos of student ?"))
i = 0
while(i < n):
    name = input("enter name ")
    marks =int(input("enter marks"))

    s = student(name, marks)
    s.display()
    s.calculate()
    i = i+1
    print("...................")
