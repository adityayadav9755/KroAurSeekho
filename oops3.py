# ------------CLASS METHOD-----------
# jb hume method me instance ki jgh class pas krni to class method bnate hain jisme self ki jgh cls argument jaata hai
class Student:
    marks = 40

    @classmethod  # class method bnane ke liye decorator
    def change(cls, newmarks):
        cls.marks = newmarks


Adi = Student()
print(Adi.marks)

Adi.change(50)  # change instance se kiya hai lekin hoga class ke liye
print(Adi.marks)

# ----------------STATIC METHOD-----------------
# jb hume instance aur class dono hi as argument na dene ho


class Employee:
    @staticmethod
    def printline(string):
        print(string)


Poi = Employee()
Poi.printline("I am intelligent")
