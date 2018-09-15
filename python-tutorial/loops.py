import random

for x in range(0, 10):
    print(x, " ", end="")

list = ["first", "second", "third"]

for e in list:
    print(e)

for x in [1, 2, 3, 4, 5]:
    print(x)

random_num = random.randrange(0, 100)

while random_num != 15:
    print(random_num)
    random_num = random.randrange(0, 100)

i = 0

while i < 20:
    print(i)
    i += 1

