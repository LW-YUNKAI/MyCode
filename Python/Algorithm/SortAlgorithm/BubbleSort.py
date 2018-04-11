import random

a = []
for k in range(20):
    a.append(random.randint(0, 100))
# 利用random.randint(0, 100)生成一个0~100的20位随机数列
print(a)


def bubble(l):
    for i in range(0, len(l)):
        for j in range(len(l)-1, i, -1):
            if l[j] < l[j-1]:
                temp = l[j]
                l[j] = l[j-1]
                l[j-1] = temp
    return l


b = bubble(a)
print(a)
