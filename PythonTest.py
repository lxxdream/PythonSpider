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

# 6 根据列表lt,实现输出: '我叫xxx，我来自xxx'
# lt = [
#     {'name':'张三', 'age':18, 'info':[('phone', '123'), ('address', '江苏南京')]},
#     {'name':'李四', 'age':19, 'info':[('phone', '789'), ('address', '浙江杭州')]},
#     {'name':'赵钱', 'age':20, 'info':[('phone', '456'), ('address', '湖北武汉')]},
#     {'name':'孙李', 'age':21, 'info':[('phone', '000'), ('address', '广东深圳')]},
#     {'name':'王五', 'age':22, 'info':[('phone', '111'), ('address', '河南洛阳')]},
# ]

# for i in lt:
#     print('我叫%s, 我来自%s' %(i['name'], i['info'][1][1]))

# 7 使用循环，实现模拟钟表 输入小时、分钟、秒，输出下一秒的时间
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

# 8 输入m，n，打印m行n列表格，表格里面的内容从1开始，先横再纵
# m = int(input('m='))
# n = int(input('n='))
# for i in range(1, m * n + 1):
#     print(i, end = ' ')
#     if i % n == 0 :
#         print('')

# 9 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%2d' %(j, i, j * i), end =' ')
#     print()


#10 定义函数,生成纯数字验证码(预设4位数)  
# import random

# def Code1(num = 4):
#     code_list = []
#     for i in range(num):
#         code_list.append(str(random.randint(0, 9)))

#     return " ".join(code_list)

# print(Code1())

# def Code2(num = 4):
#     num_list = '0123456789'
#     code_list = random.sample(num_list, num)

#     return "".join(code_list)

# print(Code2())

# 11 模拟计算器(+-*/)
# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# def mul(a, b):
#     return a * b
# def div(a, b):
#     return a / b

# a = int(input('请输入第一个数:'))
# b = int(input('请输入第二个数:'))
# fuhao = input('请选择运算符号(+ - * /):')

# if fuhao == '+':
#     print(add(a, b))
# elif fuhao == '-':
#     print(sub(a, b))
# elif fuhao == '*':
#     print(mul(a, b))
# elif fuhao == '/':
#     print(div(a, b))


# 12 归属地查询  输入手机号,匹配归属地(根据前七位)
# string = '''5582|1860101|010|北京市|北京联通GSM卡
#             5583|1860100|010|北京市|北京联通GSM卡
#             5584|1368141|010|北京市|北京移动神州行卡
#             5585|1860111|010|北京市|北京联通GSM卡
#             5586|1358198|010|北京市|北京移动动感地带卡
#             5587|1361139|010|北京市|北京移动预付费卡
#             5588|1361138|010|北京市|北京移动神州行卡
#             5591|1360110|010|北京市|北京移动全球通卡
#             5748|1364110|010|北京市|北京移动神州行卡
#             10186|1581584|020|广东省广州市|广东移动全球通卡
#             15046|1391897|021|上海市|上海移动全球通卡
#             17250|1502207|022|天津市|天津移动全球通卡
#             21137|1345272|023|重庆市万州|重庆移动大众卡
#             22700|1347812|024|辽宁省沈阳市|辽宁移动大众卡
#             24256|1377065|025|江苏省南京市|江苏移动全球通卡
#             26360|1898606|027|湖北省武汉市|湖北电信CDMA卡
#             28709|1860802|028|四川省成都市|四川联通GSM卡
#             30641|1552961|029|陕西省西安市|陕西联通GSM卡
#             31700|1563007|0310|河北省邯郸市|河北联通GSM卡
#             33360|1583396|0311|河北省石家庄市|河北移动全球通卡
#             34825|1508122|0312|河北省保定市|河北移动全球通卡
#             35363|1551235|0313|河北省张家口|河北联通GSM卡1860101
#             37700|1331326|0316|河北省廊坊市|河北电信CDMA卡
#             43500|1350358|0358|山西省吕梁市|山西移动全球通卡
#             43908|1553625|0359|山西省运城市|山西联通GSM卡
#             44521|1335360|0370|河南省商丘市|河南电信CDMA卡
#             50078|1509369|0378|河南省开封市|河南移动全球通卡
#             53603|1583981|0398|河南省三门峡|河南移动全球通卡
#             53916|1335897|0410|辽宁省铁岭市|辽宁电信CDMA卡
#             55248|1554254|0411|辽宁省大连市|辽宁联通GSM卡
#             58618|1374272|0427|辽宁省盘锦市|辽宁移动全球通卡
#             58932|1554183|0429|辽宁省葫芦岛|辽宁联通GSM卡
#             60268|1340475|0431|吉林省长春市|吉林移动大众卡'''

# stringList = string.splitlines()

# area = {}
# for string in stringList:
#     lt = string.split('|')
#     phone = lt[1]
#     local = lt[-1]
#     area[phone] = local

# print(area)
    
# while True:
#     phone = input('phone:')

#     head = phone[0:7]

#     if head in area:
#         print('area:%s' %area[head])
#     else:
#         print('None!')


# 13 自己封装函数,实现相同于系统内置函数hex、oct、bin的功能 
# def my_hex1(n):
#     lt = []
#     while n:
        
#         n, yushu = divmod(n, 16)
#         lt.append(str(yushu))

#     lt.reverse()
#     return '0x'+ ''.join(lt)

# print(my_hex1(18))

# # %d 有符号整数(十进制)
# # %u 无符号整数(十进制)
# # %o 无符号整数(八进制)
# # %x 无符号整数(十六进制)
# # %X 无符号整数(十六进制大写字符)
# def my_hex2(n):

#     return '0x' + '%X' % n

# print(my_hex2(255))































































































