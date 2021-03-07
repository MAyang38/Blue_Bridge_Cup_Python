'''
问题描述
杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)i的展开式的系数。

它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加
　　
下面给出了杨辉三角形的前4行：

   1
  1 1
 1 2 1
1 3 3 1

　　
给出n，输出它的前n行。
输入格式
输入包含一个数n。

输出格式
输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一个空格分隔。请不要在前面输出多余的空格。

样例输入
4

样例输出
1
1 1
1 2 1
1 3 3 1
'''
def yanghui():
    line = [1]
    while True:
        yield line
        line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]


def run():
    n = int(input())
    flag = 0

    for i in yanghui():
        #print(i)
        print(" ".join(str(j) for j in i))
        flag += 1
        if flag == n:
            break


if __name__ == '__main__':
    run()
    # line=[1]+[1]
    # print(line)