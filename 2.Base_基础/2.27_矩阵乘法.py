'''
问题描述
　　给定一个N阶矩阵A，输出A的M次幂（M是非负整数）
　　例如：
　　A =
　　1 2
　　3 4
　　A的2次幂
　　7 10
　　15 22
输入格式
　　第一行是一个正整数N、M（1<=N<=30, 0<=M<=5），表示矩阵A的阶数和要求的幂数
　　接下来N行，每行N个绝对值不超过10的非负整数，描述矩阵A的值
输出格式
　　输出共N行，每行N个整数，表示A的M次幂所对应的矩阵。相邻的数之间用一个空格隔开
样例输入
2 2
1 2
3 4
样例输出
7 10
15 22

'''


def multi_rect (rect_1, shape_1, rect_2, shape_2):
    if shape_1[1] != shape_2[0]:
        return
    rect_ = [[0 for _ in range(shape_2[1])] for _ in range(shape_1[0])]
    shape_ = (shape_1[0], shape_2[1])
    for i in range(shape_1[0]):
        for k in range(shape_2[1]):
            for j in range(shape_1[1]):
                rect_[i][k] += rect_1[i][j] * rect_2[j][k]
    return rect_, shape_


n, m = map(int, input().split())
rect = [[] for _ in range(n)]

for i in range(n):
    arr = input().split()
    for j in range(n):
        rect[i].append(int(arr[j]))

result, shape = rect, (n, n)

if m == 0:
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        result[i][i] = 1
else:
    for _ in range(m - 1):
        result, shape = multi_rect(rect, (n, n), result, shape)


for i in range(shape[0]):
    for j in range(shape[1]):
        print(result[i][j], end=' ')
    print()