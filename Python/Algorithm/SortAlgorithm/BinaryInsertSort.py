import random

a = []
for k in range(6):
    a.append(random.randint(0, 100))
# 利用random.randint(0, 100)生成一个0~100的20位随机数列
print(a)


def BinaryInsertSort(l):
    for i in range(1, len(l)):  # i从1开始增加遍历，直到i<list长度
        temp = l[i]
        low = 0
        high = i - 1
        while low <= high:  # 循环查找插入位置
            mid = (low + high) // 2
            if l[mid] > temp:
                high = mid - 1
            else:
                low = mid + 1

        for j in range(i-1, high, -1):  # 进行插入，插入位置是high+1
            l[j + 1] = l[j]
        l[high+1] = temp

    return l


b = BinaryInsertSort(a)
print(b)
