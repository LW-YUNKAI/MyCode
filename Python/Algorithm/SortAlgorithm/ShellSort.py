import random

a = []
for k in range(20):
    a.append(random.randint(0, 100))
# 利用random.randint(0, 100)生成一个0~100的20位随机数列
print(a)


def shellSort(l):
    dk = len(l)
    while dk > 1:
        dk = dk//2                               # 取步长循环，每次除以2
        for i in range(dk, len(l)):              # 开始进行调整位置
            temp = l[i]
            if l[i] < l[i - dk]:
                j = i - dk
                while j >= 0 and temp < l[j]:    # 跟自己的步长位置比较排序
                    l[j + dk] = l[j]
                    j = j - dk
                l[j + dk] = temp
    return l


b = shellSort(a)
print(b)
