'''
问题描述
　　求出区间[a,b]中所有整数的质因数分解。
输入格式
　　输入两个整数a，b。
输出格式
　　每行输出一个数的分解，形如k=a1a2a3…(a1<=a2<=a3…，k也是从小到大的)(具体可看样例)
样例输入
3 10
样例输出
3=3
4=22
5=5
6=23
7=7
8=222
9=33
10=25

'''
from math import sqrt


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a, b = map(int, input().split())
for i in range(a, b+1):
    if is_prime(i):
        print(i, '=', i, sep='')
    else:
        print(i, '=', sep='', end='')
        temp = i
        j = 2
        while temp > 1:
            if temp % j == 0:
                temp = int(temp/j)
                print(j, end='')
                if temp != 1:
                    print('*', end='')
            else:
                j += 1
        print()