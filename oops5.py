class Student:
    marks = 10
    score = 10
    pay = 10

    def __init__(self, name, sec):
        self.name = name
        self.section = sec

    def printdetails(self):
        return f"{self.name} studies in class XII {self.section}"

    @classmethod
    def from_slash(cls, string):
        lis = string.split("/")
        return cls(lis[0], lis[1])

    @classmethod
    def oneliner(cls, string):
        return cls(*string.split("/"))


Adi = Student.from_slash("Aditya/A")
Haathi = Student.oneliner("Aadesh/A")

# -------------------SINGLE INHERITANCE---------------------


class Player(Student):  # Student class ke sabhi variables aur methods ab Player class access kr skti hai
    # yeh Student class ka constructor as default use krega
    score = 11
    pay = 11
    def game_list(self, games):
        return f"{self.name} plays {games}"


Om = Player("Om", "A")
print(Om.game_list(["basketball", "coding"]))


# --------------------MULTIPLE INHERITANCE------------------

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def printdetials(self):
        return f"{self.name} works as {self.role}"


class CoolBoy(Student, Employee):  # Order important hai. Student class ko priority dega
    def some(self):
        print("I'm a cool boy.")


Yash = CoolBoy("Yash", "A")
print(Yash.printdetails()) # student waala method chalega kyunki uski priority zyada hai

# ----------------------MULTILEVEL INHERITANCE-------------------------


class Awesome(Player):  # Awesome inherits Player which itself inherits Student
    pay = 12


Divy = Awesome("Divyansh", "A")
print(Divy.pay, Divy.score, Divy.marks)
