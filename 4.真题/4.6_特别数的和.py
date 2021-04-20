'''

'''
n = int(input())
s = 0
for i in range(1, n + 1):
    a = i
    while a != 0:
        temp = a % 10
        a = int(a/10)
        if temp in [2, 0, 1, 9]:
            s += i
            flag = True
            break

print(s)