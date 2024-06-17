l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

i = 1
for item in l1:
    if i % 2 != 0:
        print(f"to buy {item}")
    i += 1

# above and below code do the same thing

for index, item in enumerate(l1):
    if index % 2 == 0:
        print(f"to buy {item}")

