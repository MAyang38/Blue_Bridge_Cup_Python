'''
问题描述
　　平面上有两个矩形，它们的边平行于直角坐标系的X轴或Y轴。对于每个矩形，我们给出它的一对相对顶点的坐标，请你编程算出两个矩形的交的面积。
输入格式
　　输入仅包含两行，每行描述一个矩形。
　　在每行中，给出矩形的一对相对顶点的坐标，每个点的坐标都用两个绝对值不超过10^7的实数表示。
输出格式
　　输出仅包含一个实数，为交的面积，保留到小数后两位。
样例输入
1 1 3 3
2 2 4 4
样例输出
1.00

'''
rect_1 = list(map(float, input().split()))
rect_2 = list(map(float, input().split()))
area = 0

x1 = max(min(rect_1[0], rect_1[2]), min(rect_2[0], rect_2[2]))
y1 = max(min(rect_1[1], rect_1[3]), min(rect_2[1], rect_2[3]))
x2 = min(max(rect_1[0], rect_1[2]), max(rect_2[0], rect_2[2]))
y2 = min(max(rect_1[1], rect_1[3]), max(rect_2[1], rect_2[3]))
#
# area = abs((x2 - x1)*(y2 - y1))
# print('%.2f' %area)

if x1 < x2  and y1 < y2:
    area = (x2 - x1)*(y2 - y1)
    print('%.2f' % area)
else:
    print('%.2f' %area)


