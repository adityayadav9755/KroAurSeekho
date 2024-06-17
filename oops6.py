# Public - koi bhi access kr skta hai
# Protected - khud aur derived class access kr skte hain
# Private - sirf khud access kr skta hai

class Student:
    name = "naam"  # Public
    _sec = "section"  # Protected phir bhi print ho jaega
    __tran = "id"  # Private (naam hi badal ke save hota hai: _classname__variablename)


class Player(Student):
    games = ['Cricket']


Adi = Student()
Amay = Player()

print(Adi.name, Adi._sec, Adi.__tran)
print(Amay._sec)
