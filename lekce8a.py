class Person:
    def __init__(self, name, surname, age):

        self.name = name
        self.surname = surname
        self.age = age

    def showMsg(self):
        print(f"Jmeniji se {self.name} {self.surname} a je mi {self.age}")

clovek1 = Person ("Pavel", "Novak" , 45 )
clovek1.showMsg()

class Student (Person):
    # spec = "devOps"
    def __init__(self, name, surname, age, spec):
        super().__init__(name, surname, age)
        self.spec = spec


student1 = Student ("Pavel", "Novak" , 45, "HW" )
print (student1.spec)