# coding:utf-8
import sys
# print(sys.getdefaultencoding())
# print(sys.stdin.encoding)
# print(sys.stdout.encoding)
# print(sys.stderr.encoding)

''' 
print("Hello World 你好世界")
print("ddddd")
print("弟弟")
print("test")
print("hehe")
print("on jack's mbp")
print("test vscode git")
print("another test")
print("tortoise git test")

a = 1
b = 2
print(a+b)
'''

# 1 输入一个3位数，计算个位、百位、十位
''' a = int(input("请输入一个3位数:"))
if a < 100 or a > 999:
    print("不是正确的数字")
else:
    print(a%10, (a//10)%10, (a//100))
    print(a%10*100 + (a//10)%10*10 + (a//10//10)) '''

# 2 输入一个年份，判断是否是闰年(能被4整除但是不能被100整除或者能够被400整除的年份)
''' a = int(input("请输入一个年份:"))
if (a%4 == 0 and a%100 != 0) or a%400 == 0:
    print("是闰年")
else:
    print("不是闰年") '''

# 3 计算1-100的和（5050）
''' sum = 0
for i in range(1, 101):
    sum += i
print(sum) '''

# 4 打印字母A-Z 每5个字母一行
# count = 0
# for i in range(ord('A'), ord('Z') + 1):
#     count += 1
#     print(chr(i), end = ' ')
#     if count%5 == 0:
#         print('')
# print('')

# 5 打印字母Z-A 每5个字母一行
lt = []
for i in range(ord('A'), ord('Z') + 1):
    lt.append(chr(i))
print(lt)
lt.reverse()
print(len(lt))
for i in range(0, len(lt)):
    print(lt[i], end = ' ')
    if i%4 == 0:
        print('')
print('')
print(type(lt[0]))









