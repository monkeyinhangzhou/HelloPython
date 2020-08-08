import stdio
import math
import random
# 字符串拼接
ruler1 = '1'
ruler2 = ruler1 + ' 2 ' + ruler1
ruler3 = ruler2 + ' 3 ' + ruler2
ruler4 = ruler3 + ' 3 ' + ruler3
ruler5 = ruler4 + ' 3 ' + ruler4
stdio.writeln(ruler1)
stdio.writeln(ruler2)
stdio.writeln(ruler3)
stdio.writeln(ruler4)
stdio.writeln(ruler5)

# str(123) 将123转为字符串
stdio.writeln('123')
stdio.writeln(str(123))
stdio.writeln(str(1) + '+' + str(2) + '=' + str(1+2))

# 字符串转数值: float(),int()
x=1.5+float("1.5")
stdio.writeln(x)

# ============================================
# 整数int的运算符 + - * //(整除,小数部分舍弃) %(取模) **(乘幂)
# int类型任意大,受限于计算机系统可用内存

# 浮点数float的运算符 + - * / **
# 浮点数精度在15~17位有效数字

#整数和浮点数相互转化 round() 在Python3中返回整数,Python2中返回浮点数
round(1.6)

#常用函数
x=1
y=2
abs(x)
max(x,y)
min(x,y)
math.sin(x)#正弦
math.cos(x)#余弦
math.tan(x)#正切
math.atan2(x,y)#点(y,x)的极角
math.hypot(x,y)#点(x,y)到远点的距离
math.radians(x)#将x角度转换为弧度
math.degrees(x)#将x弧度转换为角度
math.exp(x)#x的指数函数
math.log(x,y)#x以y为底的对数
math.sqrt(x)#x的平方根
math.erf(x)#x的误差函数
math.gamma(x)#x的伽玛函数
math.pi# π
stdio.writeln(math.pi)
random.random()#[0-1)区间随机浮点数
random.randrange(x,y)#返回[x,y)区间随机整数,

#单引号,双引号,三引号
s="""Python's "triple" quotes 
are useful to 
specify string literals 
that span 
multiple lines """

#python的变量是无类型的.同一个变量可以绑定不同的数据类型的对象
#type()返回对象类型
#id()#返回对象id
#repr()#返回一个对象明确的字符串表示形式
a=math.pi
id(a)
type(a)
repr(a)


#python支持任意长度的链式比较
stdio.writeln(1>2>4>3)#false
#支持任意长度赋值语句
a=b=c=1
#0, 0.0, 空字符串'' 都被视为false,其他整数,浮点数,字符串则视为True
#True和False可被转化为1和0
x=(False-True-True)*True
#if
if 0==1:
    pring(1)
else:
    print(2)

if 0<1:
    print(1)
elif 0>1:
    print(2)
elif 0==1:
    print(1)

#while
i=0
while i<1:
    print(1)
    i+=1
    if i == 0:
        break

for item in range(1,10):
    print(item)

x=1
x=2*x
x*=2

# \ 是续行符
print(False==True==False==True)

# 数组
suits = ['Clubs','Diamonds','Hearts','Spades']
x=[0.30,0.60,0.10]
y=[0.40,0.10,0.50]
#如果数组x[]和y[]分别表示两个向量,则其点积的表达式为
z=x[0]*y[0]+x[1]*y[1]+x[2]*y[2]
print(x)
len(x)#数组的长度

a=[1,2,3]
a+=[4]
#a=[1,2,3,4]

a=[]
for i in range(10):
    a += [0.0]
stdio.writeln(a)
stdio.writeln(len(a))#10
x=0
for i in a:
   x += i

# 数组别名:通过x改变数组会影响y,因为x,y指向是一个数组,
x=[.30,.60,.10]
y=x
x[1]=.99
print(y[1])

#数组x[]复制到数组y[]
y=[]
for i in x:
    y += [i]

#数组切片
#创建一个新数组,包含元素为a[i],...a[j-1]
#i默认值为0,j默认值为len(a)
a[i:j]
a[:]
#虽然简洁,但是开销很大
y = x[:]





























