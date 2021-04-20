'''
问题描述

如果一个自然数N的K进制表示中任意的相邻的两位都不是相邻的数字，那么我们就说这个数是K好数。求L位K进制数中K好数的数目。例如K = 4，L = 2的时候，所有K好数为11、13、20、22、30、31、33 共7个。由于这个数目很大，请你输出它对1000000007取模后的值。
输入格式

输入包含两个正整数，K和L。
输出格式
输出一个整数，表示答案对1000000007取模后的值。
样例输入
4 2
样例输出
7
数据规模与约定

对于30%的数据，KL <= 106；

对于50%的数据，K <= 16， L <= 10；

对于100%的数据，1 <= K,L <= 100。
'''

def count(legth, kind, ans):
    for i in range(1, kind):
        dp[0][i] = 1
    for i in range(1, legth):
        for j in range(kind):
            for k in range(kind):
                if abs(j - k) != 1:
                    if j - 1 == 0 and k == 0:
                        continue
                    dp[i][j] = dp[i][j] + dp[i - 1][k]
                    dp[i][j] %= MOD
    for i in range(kind):
        # print(dp[legth - 1][i])
        ans += dp[legth - 1][i]
        ans %= MOD
    return ans

K, L = map(int, input().split())
ans = 0
MOD = 1000000007
dp = [[0 for _ in range(max(L, K))] for _ in range(max(L, K))]
if K == 1 and L == 1:
    print(0)
elif K > 1 and L == 1:
    print(K)
elif L > 1:
    print(count(L, K, ans))
# for i in range(K):
#     for j in range(K):
#         print(dp[i][j],end='')
#     print()

# MOD = 1000000007
# K, L = map(int, input().split())
# if K == 1 and L == 1:
#     print(0)
#     exit()
# elif K > 1 and L == 1:
#     print(K)
#     exit()
# num = [[0 for i in range(L)] for j in range(K)]
#
# for i in range(K):
#     num[i][0]=1
# for j in range(L-1):
#     for i in range(K):
#         tmp = 0
#         for k in range(K):
#             if k == i or abs(k-i) != 1:
#                 tmp += num[k][j]
#                 tmp %= MOD
#         num[i][j+1] = tmp
# ans = 0
# for i in range(1, K):
#     ans += num[i][L-1]
#     ans %= MOD
# print(ans)
