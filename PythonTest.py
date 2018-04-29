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


# ---------------------------------------------------------------------------------------------------------------------------------


# 1 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# lt =[]
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != j) and (i != k) and (j != k):
#                 #print(i, j, k)
#                 lt.append(str(i)+str(j)+str(k))
# print(lt)

# lt = []
# for i in range(123, 433):
#     a = (i // 100)
#     b = (i // 10) % 10
#     c = i % 10
#     if (a != b) and (a != c) and (b != c) and (0 < a < 5) and (0 < b < 5) and (0 < c < 5):
#         print(i)
#         lt.append(i)

# list_num = [1, 2, 3, 4]
# lt = [i * 100 + j * 10 + k for i in list_num for j in list_num for k in list_num if i != j and i != k and j != k]
# print(lt)

# list_num = [1, 2, 3, 4]
# for i in list_num:
#     list1 = list_num.copy()
#     list1.remove(i)
#     for j in list1:
#         list2 = list1.copy()
#         list2.remove(j)
#         for k in list2:
#             print(i, j, k)

# from itertools import permutations

# # permutations(p[,r]);返回p中任意取r个元素做排列的元组的迭代器
# for i in permutations([1, 2, 3, 4], 3):
#     print(i)


# ---------------------------------------------------------------------------------------------------------------------------------


# 2 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%;
# 高于100万元时，超过100万元的部分按1%提成,
# 从键盘输入当月利润I，求应发放奖金总数


# def Bonus(x):
#     bonus = 0
#     if x <= 100000:
#         bonus = x * 0.1
#     elif 100000 < x <= 200000:
#         bonus = 10000 + (x - 100000) * 0.075
#     elif 200000 < x <= 400000:
#         bonus = 10000 + 7500 + (x - 200000) * 0.05
#     elif 400000 < x <= 600000:
#         bonus = 10000 + 7500 + 10000 + (x - 400000) * 0.03
#     elif 600000 < x <= 1000000:
#         bonus = 10000 + 7500 + 10000 + 6000 + (x - 600000) * 0.015
#     else:
#         bonus = 10000 + 7500 + 10000 + 6000 + 6000 + (x - 1000000) * 0.01

#     return bonus
    
# num = int(input("净利润："))
# print("奖金为：", Bonus(num))

# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# total = 0
# for i in range(0, 6):
#     if num > arr[i]:
#         temp = (num - arr[i]) * rat[i]
#         print(temp)
#         total += temp
#         num = arr[i]
# print(total)

# total = 0
# rate_list = [[1000000, 0.01], [600000, 0.015], [400000, 0.03], [200000, 0.05], [100000, 0.075] ,[0, 0.1]]
# for i in range(len(rate_list)):
#     if num > rate_list[i][0]:
#         temp = (num - rate_list[i][0]) * rate_list[i][1]
#         print(temp)
#         total += temp
#         num = rate_list[i][0]
# print(total)

# def get_reward(x):
#     rewards = 0
#     if x <= 10:
#         rewards = x * 0.1
#     elif 10 < x <= 20:
#         rewards = get_reward(10) + (x - 10) * 0.075
#     elif 20 < x <= 40:
#         rewards = get_reward(20) + (x - 20) * 0.05
#     elif 40 < x <= 60:
#         rewards = get_reward(40) + (x - 40) * 0.03
#     elif 60 < x <= 100:
#         rewards = get_reward(60) + (x - 60) * 0.015
#     else:
#         rewards = get_reward(100) + (x - 100) * 0.01

#     return rewards

# print(get_reward(num / 10000) * 10000)


# ---------------------------------------------------------------------------------------------------------------------------------


# 3 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# x^2 + 168 = y^2，则x、y都小于168，而且x应小于y
for y in range(168):
    for x in range(y):
        if y**2 - x**2 == 168:
            n = x**2 - 100
            print(n)

'''1、则：x + 100 = n2, x + 100 + 168 = m2

2、计算等式：m2 - n2 = (m + n)(m - n) = 168

3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数

4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。

5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。

6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。

7、接下来将 i 的所有数字循环计算即可。'''
# for i in range(2, 85):
#     if 168 % i == 0:
#         j = 168 / i
#         if (i > j) and (i + j) % 2 == 0 and (i - j) % 2 == 0:
#             m = (i + j) / 2
#             n = (i - j) / 2
#             print(m)
#             print(n)
#             x = n * n - 100
#             print(x)

'''设该数为x：x + 100 = n^2, n^2 + 168 = m^2。

设m=n+k（不妨设m,n,k均为自然数）：带入m^2-n^2-168，得k^2+2nk=168。

解得n=84/k - k/2；由于n,k均为自然数，则nk>=1，故1< =k^2<168，故1<=k<=12。'''
# for k in range(1, 13):
#     n = 84 / k -  k / 2
#     print(n)
#     if int(n) == n:
#         x = n ** 2 - 100
#         print(int(x))

'''设该数为x：x + 100 = n^2, n^2 + 168 = m^2。

设m=n+k（不妨设m,n,k均为自然数）：带入m^2-n^2-168，得k^2+2nk=168。

在此基础上 k(k+2n)=168 , 若 k为奇数，k+2n也为奇数，等式不成立，所以k为偶数，

则等式除以4,得(k/2)(k/2+n) =42， 令 t=k/2, (t>0)   

t(t+n)=42  则 n= 42/t -t ; 由于n大于0，所以 t小于等于6 ，42/t 又是整数，得到 t 的取值为 1,2,3,6,

对应得到 x =1581,261,21，-99'''


'''
x+100=n^2和x+100+168=m^2
推出  m^2-n^2=168
即   （m+n)(m-n)=168
设    m+n=i m-n=j
则    i*j=168
由    i>0 j>0   推出  i%2=0 j%2=0 ?????
由    168=2*2*2*3*7
上面两个条件推出i与j值的范围[2,4,6,12,14,28,42,84]
反推：m=(i+j)/2和n=(i-j)/2 并且 n>0 推得 i>j
则     i=[14,28,42,84]
       j=[12,6,4,2]
'''
# for m in range(-168,169):
#     for n in range(-168,169):
#         if (m+n)*(m-n)==168:#m,n都是整数
#             print(n**2-100)

'''斐波那契数列'''
nums = [1, 1]
for i in range(2, 101):
    nums.append(nums[i-1]+nums[i-2])
print(nums)
















































































