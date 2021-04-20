m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]
row = 0
col = 0
count = 0
while count < m*n:
    while row < m and data[row][col] != -1:
        print(data[row][col], end=' ')
        data[row][col] = -1
        row += 1
        count += 1
    row -= 1
    col += 1
    while col < n and data[row][col] != -1:  # 向右
        print(data[row][col], end=' ')
        data[row][col] = -1
        col += 1
        count += 1
    row -= 1
    col -= 1
    while row >= 0 and data[row][col] != -1:
        print(data[row][col], end=' ')
        data[row][col] = -1
        row -= 1
        count += 1
    row += 1
    col -= 1
    while col >= 0 and data[row][col] != -1:
        print(data[row][col], end=' ')
        data[row][col] = -1
        col -= 1
        count += 1
    col += 1
    row += 1
