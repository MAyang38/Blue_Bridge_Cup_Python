'''
  一个字符串的非空子串是指字符串中长度至少为 1 的连续的一段字符组成 的串。
  例如，字符串aaab 有非空子串a, b, aa, ab, aaa, aab, aaab，一共 7 个。
   注意在计算时，只算本质不同的串的个数。

   请问，字符串0100110001010001 有多少个不同的非空子串？

'''
var = '0100110001010001'
var = 'aaab'
# print("测试", var[0:16])
length = len(var)
result = []
sum = 0
# i ：为步长
for i in range(length):
    for j in range(length - i + 1):
        # print(var[j:j+i])
        if var[j:j+i] in result:
            continue
        else:
            result.append(var[j:j+i])
            sum += 1

print(sum)