# --------------------MAP--------------
# kisi function ko list ke saare elements pe
# apply krne ke liye map use hota hai map

num = ["1", "3", "7"]
print(list(map(int, num)))

num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
sq = list(map(lambda x: x*x, num1))  # lambda ki jgh alag function bna ke uska naam likh skta hu
print(sq)

# ------------------FILTER---------------
# un values ko filter ke krke alag list me return krta hai
# jo kisi function ke liye true hain


def func(x):
    return x > 5


print(list(filter(func, num1)))

# -----------------REDUCE-------------
# pta nhi kyu but nhi kaam  kr rha reduce
# maybe version problem
