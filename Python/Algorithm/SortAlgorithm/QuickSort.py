import random


a = []
for k in range(20):
    a.append(random.randint(0, 100))
# 利用random.randint(0, 100)生成一个0~100的20位随机数列
print(a)


def quickSort(l, low, high):
    if low < high:
        pivots = partition(l, low, high)
        quickSort(l, low, pivots - 1)
        quickSort(l, pivots + 1, high)
    return l


def partition(l, low, high):
    pivot = l[low]                               # 第一个元素是作为基准值
    while low < high:                            # 开始第一轮查找
        while low < high and l[high] >= pivot:   # 从尾部找比它小的，没有high值前移
            high -= 1
        l[low] = l[high]                         # 找到了就把low值记录为high值（此处high比pivot小）
        while low < high and l[low] <= pivot:    # 从刚才的low值处往后查找比它大的
            low += 1
        l[high] = l[low]                         # 找到了把刚才的high值变为找到的low值（此low值比pivot大）
    l[low] = pivot
    return low


b = quickSort(a, 0, len(a) - 1)
print(b)
