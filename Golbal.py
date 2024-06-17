# Global(scope) variable program ka koi bhi function use kr skta hai
# Local(scope) variable program ka koi bhi function use nhi kr skta hai
# permission to change global variable in a function - "global variable_name"

n = 10  # Global


def tets():
    n, m = 5, 5  # Local
    print(n, m)


def tets2():
    global n  # yeh nhi lgaya to nhi waali line nhi chalegi
    n = n + 45
    print(n)

tets()
tets2()
