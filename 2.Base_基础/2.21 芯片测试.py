n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
# print(data)
chip = [True for _ in range(n)]
for col in range(n):
    count = 0
    for row in range(n):
        if data[row][col] == 0:
            count += 1
    if count > n/2:
        chip[col] = False
for i in range(n):
    if chip[i]:
        print(i+1, end=' ')
