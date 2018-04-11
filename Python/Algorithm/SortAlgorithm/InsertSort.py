import random

a = []
for k in range(20):
    a.append(random.randint(0, 100))
# 利用random.randint(0, 100)生成一个0~100的20位随机数列
print(a)


def insertDirectly(l):
    for i in range(1, len(l)):  # i从1开始增加遍历，直到i<list长度
        if l[i] < l[i - 1]:  # 如果，list[i]<list[i-1]证明i比已经排列好的最大一位小
            temp = l[i]  # 用temp暂时记录list[i]
            j = i - 1  # 利用j记录已经排列好的数组，即0~i-1位
            while j >= 0 and temp < l[j]:  # 循环只要j位比该值小，且未到开始，则将数据后移一位
                l[j + 1] = l[j]
                j = j - 1
            l[j + 1] = temp  # 跳出循环将该位变成需要插入的数据
    return l  # 返回新表


b = insertDirectly(a)
print(b)
