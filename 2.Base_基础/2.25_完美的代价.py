'''
问题描述
　　回文串，是一种特殊的字符串，它从左往右读和从右往左读是一样的。小龙龙认为回文串才是完美的。现在给你一个串，它不一定是回文的，请你计算最少的交换次数使得该串变成一个完美的回文串。
　　交换的定义是：交换两个相邻的字符
　　例如mamad
　　第一次交换 ad : mamda
　　第二次交换 md : madma
　　第三次交换 ma : madam (回文！完美！)
输入格式
　　第一行是一个整数N，表示接下来的字符串的长度(N <= 8000)
　　第二行是一个字符串，长度为N.只包含小写字母
输出格式
　　如果可能，输出最少的交换次数。
　　否则输出Impossible
样例输入
5
mamad
样例输出
3

'''

n = int(input())

pal = list(input())
count = flag = 0
# print(pal)

m = n - 1
if n == 1:
    print(count)
    exit()
for i in range(m):
    for k in range(m, i -1 , -1):
        # print(i, '     ', k)
        if k == i:
            if n % 2 == 0 or flag == 1:
                print('Impossible')
                exit()
            flag = 1
            count += int(n / 2) - i
        elif pal[k] == pal[i]:
            for j in range(k, m):
                pal[j], pal[j + 1] = pal[j + 1], pal[j]
                count += 1
            m -= 1
            break

print(count)
