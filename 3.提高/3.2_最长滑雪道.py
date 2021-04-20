'''
问题描述
　　小袁非常喜欢滑雪， 因为滑雪很刺激。为了获得速度，滑的区域必须向下倾斜，而且当你滑到坡底，你不得不再次走上坡或者等待升降机来载你。 小袁想知道在某个区域中最长的一个滑坡。区域由一个二维数组给出。数组的每个数字代表点的高度。如下：
　　
一个人可以从某个点滑向上下左右相邻四个点之一，当且仅当高度减小。在上面的例子中，一条可滑行的滑坡为24-17-16-1。当然25-24-23-…-3-2-1更长。事实上，这是最长的一条。
　　你的任务就是找到最长的一条滑坡，并且将滑坡的长度输出。 滑坡的长度定义为经过点的个数，例如滑坡24-17-16-1的长度是4。
输入格式
　　输入的第一行表示区域的行数R和列数C(1<=R, C<=10)。下面是R行，每行有C个整数，依次是每个点的高度h（0<= h <=10000）。
输出格式
　　只有一行，为一个整数，即最长区域的长度。
样例输入
5 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
样例输出
25

'''

def dfs(x, y):
    max_height = 1
    if dp[x][y] > 0:
        return dp[x][y]
    for k in range(4):
        tx = x + next_[k][0]
        ty = y + next_[k][1]
        if tx < 0 or tx >= row or ty < 0 or ty >= col:
            continue
        if arr[tx][ty] >= arr[x][y]:
            continue
        max_height = max(max_height, dfs(tx, ty) + 1)
    dp[x][y] = max_height

    return dp[x][y]
row, col = map(int, input().split())
dp = [[0 for _ in range(col)] for _ in range(row)]
arr = [list(map(int, input().split())) for _ in range(row)]
next_ = [[0, 1], [1, 0], [0, -1], [-1, 0]]

ans = 0
for i in range(row):
    for j in range(col):
        ans = max(ans, dfs(i, j))

print(ans)