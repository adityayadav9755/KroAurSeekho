# Class -  yeh ek template hota hai jise hum repetition avoid krne ke liye use krte hain.
# Class ka naaam Capital se shuru krna good practice.
# Object - yeh Class ka instance hota hai mtlb us template se bna koi cheez
# Example - Class: Letter to Editor ka format. Object: koi ek paricular letter.
class Student:
    school = "Sharda Vidya Mandir"  # Class Variable - yeh sabhi objects ke liye initially same rahega
    pass


std1 = Student()  # one of the objects
std2 = Student()

std1.name = "Aditya"  # Instance Variables - us particular object ke personal variable
std2.section = "B"

std1.school = "SVM"  # us object ke liye change krega(nya varible bnakar)
print(std1.__dict__, Student.__dict__)

Student.school = "SVM"  # sabhi objects ke liye change kr dega
print(std1.__dict__, Student.__dict__)
