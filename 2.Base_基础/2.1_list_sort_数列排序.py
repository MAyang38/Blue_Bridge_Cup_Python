"""
问题描述
　　给定一个长度为n的数列，将这个数列按从小到大的顺序排列。1<=n<=200
输入格式
　　第一行为一个整数n。
　　第二行包含n个整数，为待排序的数，每个整数的绝对值小于10000。
输出格式
　　输出一行，按从小到大的顺序输出排序后的数列。
样例输入
5
8 3 6 4 9
样例输出
3 4 6 8 9
"""
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
#type1
for i in range(n):
    print(arr[i],end=' ')
# #type2
# for i in range(n - 1):
#     print(arr[i], end=' ')
# print(arr[n-1])
# #type3
# for i in range(n - 1):
#     print(arr[i], end=' ')
# print(arr[n-1], end='')