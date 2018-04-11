import math


def C(n, m):
    return math.factorial(n) / (math.factorial(m) * math.factorial(n - m))


def rPOut(n, m):
    if n > m:
        res = 0.0
        for i in range(m):
            res += C(n, (i+1))*((i+1)/n)**m
        return res
    else:
        res = 0.0
        for i in range(n):
            res += C(n, (i + 1)) * ((i + 1) / n) ** m
        return res


if __name__ == '__main__':
    print(C(3, 2))
    print(rPOut(5, ))
