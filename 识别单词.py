import collections
import sys,os

with open(u'文本单词测试.txt') as file1:
    file2 = file1.read().split()
# print("原文本：%r"%file2)
# print("各单词出现的次数：\n %r" % collections.Counter(file2))
# print("原文本：%r"%file2[0])
result = []
for i in file2:
    for j in i:
        result.append(j)
# print(len(result))
# print(collections.Counter(result))
# print(len(file2))
# num = collections.Counter(result)
# print(len(num))
# print(type(num))
# print(''.join(result))
num1 = ''.join(result)
print(type(num1))
zizifu='萧晋寒'
count=0
for i in range(len(num1)-1):
    if num1[i:i+len(zizifu)] ==zizifu:
        count +=1
        num1=num1[:i]+"替换功能"+ num1[i+len(zizifu):]
print("文本中出现%r的次数："%zizifu,count)
