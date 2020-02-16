import random

num_list = []
for x in range(10):
    num = random.randint(1, 20)
    num_list.append(num)
    print(num_list)

num_list = "".join(map(str , num_list))
print(num_list)
