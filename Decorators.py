# --------------Extra Gyaan--------------
# def f1():
#     print("a")
# f2 = f1
# del f1   : deletes the function
# f2()     : abhi bhi 'a' print ho jayega

# ----------DECORATORS-----------------
# decorators ki madad se hum koi operation multiple functions pe chla skte hain according to our need

def dec1(func):
    def karo():
        print(f"the output of your function is")
        func()
    return karo()


def a():
    print("Aditya\n")


a()  # bina decorator lgaye output


@dec1    # decorator 'b' function pe lgane ka tareeka
def b():
    print("Aditya")  # decorator lga ke output
