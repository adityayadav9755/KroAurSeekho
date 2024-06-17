class Student:
    # Constructor function - yeh clss ke construction me help krta hai
    def __init__(self, studid, studname, studclass, studsec, studrn):  # Object ka naam as self argument jaata hai
        """

        :param studid: student ki id
        :param studname: student ka naam
        :param studclass: student ki class
        :param studsec: student ka section
        :param studrn: student ka roll no
        """
        self.id = studid
        self.name = studname
        self.standard = studclass
        self.section = studsec
        self.rollno = studrn


stud1 = Student("5154", "Aditya", "XII", "A", 12)
print(stud1.__dict__)
print(stud1.name)
