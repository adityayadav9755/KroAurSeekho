# --------ALTERNATIVE CONSTRUCTOR--------------
# class method ko alternative constructor ki trh bhi use kr skte hain

class Student:
    def __init__(self, name, sec):
        self.name = name
        self.section = sec

    @classmethod
    def from_slash(cls, string):
        lis = string.split("/")
        return cls(lis[0], lis[1])

    @classmethod
    def oneliner(cls, string):  # same upar waali cheez krne ka one liner tareeka
        return cls(*string.split("/"))  # '*args' used


Adi = Student.from_slash("Aditya/A")
print(Adi.__dict__)

Haathi = Student.oneliner("Aadesh/A")
print(Haathi.__dict__)
