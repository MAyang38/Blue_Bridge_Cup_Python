'''
 把 2019 分解成 3 个各不相同的正整数之和，并且要求每个正整数都不包含数字 2 和 4，一共有多少种不同的分解方法？

   注意交换 3 个整数的顺序被视为同一种方法，例如 1000+1001+18 和 1001+1000+18 被视为同一种。
'''
count = 0

def check(x):
    while x != 0:
        t = x % 10
        x = int(x / 10)
        if t == 2 or t ==4:
            return False
    return True

for i in range(1, 2019):
    if check(i):
        for j in range(i+1, 2019):
            if check(j):
                k = 2019 - i - j
                if k > j and check(k):
                    count += 1
                    print(i, j, k)
print(count)