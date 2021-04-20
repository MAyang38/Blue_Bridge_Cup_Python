"""

要在n*n的国际象棋棋盘中放n个皇后，
使任意两个皇后都不能互相吃掉。
规则：皇后能吃掉同一行、同一列、同一对角线的任意棋子。
求所有的解。
n=8是就是著名的八皇后问题了。

"""
maxsum = 0


def queen(A, cur=0):
    global maxsum
    if cur == len(A):
        # print(A)
        sum = my_Max(A, data)
        if sum > maxsum:
            maxsum = sum
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A, cur + 1)

def my_Max(A, data):
    sum = 0
    for i in range(8):
        sum += data[i][A[i]]
    return sum

# n = int(input())
data = [list(map(int, input().split())) for _ in range(8)]
queen([None]*8)
print(maxsum)