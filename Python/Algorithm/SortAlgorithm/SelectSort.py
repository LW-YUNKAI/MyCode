import random

a = []
for k in range(20):
    a.append(random.randint(0, 100))
print(a)


def selectSort(l):
    for i in range(0, len(l) - 1):
        minNum = i
        for j in range(i + 1, len(l)):
            if l[j] < l[minNum]:
                minNum = j
        if l[minNum] != l[i]:
            temp = l[i]
            l[i] = l[minNum]
            l[minNum] = temp
    return l


b = selectSort(a)
print(b)
