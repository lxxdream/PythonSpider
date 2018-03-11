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
# lt = []
# for i in range(ord('A'), ord('Z') + 1):
#     lt.append(chr(i))
# print(lt)
# lt.reverse()
# print(len(lt))
# for i in range(0, len(lt)):
#     print(lt[i], end = ' ')
#     if i%4 == 0:
#         print('')
# print('')
# print(type(lt[0]))

#6 根据列表lt,实现输出: '我叫xxx，我来自xxx'
# lt = [
#     {'name':'张三', 'age':18, 'info':[('phone', '123'), ('address', '江苏南京')]},
#     {'name':'李四', 'age':19, 'info':[('phone', '789'), ('address', '浙江杭州')]},
#     {'name':'赵钱', 'age':20, 'info':[('phone', '456'), ('address', '湖北武汉')]},
#     {'name':'孙李', 'age':21, 'info':[('phone', '000'), ('address', '广东深圳')]},
#     {'name':'王五', 'age':22, 'info':[('phone', '111'), ('address', '河南洛阳')]},
# ]

# for i in lt:
#     print('我叫%s, 我来自%s' %(i['name'], i['info'][1][1]))

#8 使用循环，实现模拟钟表 输入小时、分钟、秒，输出下一秒的时间
# import time

# while True:
#     hour = int(input('hout:'))
#     minute = int(input('minute:'))
#     second = int(input('second:'))

#     if (hour < 0 or hour >= 24) or (minute < 0 or minute >=60) or (second < 0 or second >= 60):
#         print('Wrong!! Please input again')
#         continue
    
#     while True:
#         time.sleep(1)
#         second += 1

#         if (second == 60):
#             second = 0
#             minute += 1

#         if (minute == 60):
#             minute = 0
#             hour += 1

#         if (hour == 24):2
#             hour = 0

#         print('%02d:%02d:%02d' %(hour, minute, second))

# 9 输入m，n，打印m行n列表格，表格里面的内容从1开始，先横再纵
# m = int(input('m='))
# n = int(input('n='))
# for i in range(1, m * n + 1):
#     print(i, end = ' ')
#     if i % n == 0 :
#         print('')

#10 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%2d' %(j, i, j * i), end =' ')
    print()


























































