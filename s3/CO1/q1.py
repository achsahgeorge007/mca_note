#addition of two numbers
print(10+5)
#substraction of two numers
print(10-5)
# product of two numbers
print(10*5)
# Quotient of two numbers
print(10/5)
# power of a number
print(10**5)
# modulus of two numbers
print(10%5)
# Strings
"Hai"
#variable assignment
x=10
y=5
z=x+y
print(z)
#list
li=[1,2,3,4,5]
li.append(6)
print(li)
print(li[3])
print(li[0:2])
print(li[2:])
#dictionary,,,,,,,,,,,,,
d={'key1':'item1','key2':'item2','key3':'item3'}
print(d)
print(d['key2'])
#comparison
print(10>5)
print(10<5)
#tuple............
t=(1,2,3,4,5)
print(t)
print(t[1])
#sets...........
s={1,2,3,4,5,6,7}
print(s)
print("loop")
#loop...........
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
  print(i)
i=1
print("loop")
while i<7 :
  print(i)
  i=i+1
  print(i)
#logic operations..............
print("logic operations")
print((1>2)or(2<3))
print("logic operations")
print((3>4)and(4<5))
#if else,,,,,,,,,,
if 2>3:
  print('false')
else:
  print('true')
#if else if..............
if(1==2):
  print('equal')
elif(1<2):
  print("small")
else:
  print("large")
#functions,,,,,,,,,,,
def fun(param1="default"):
  print(param1)
fun()
def square(a):
  print(a*a)
square(5)
#lamdaa...............
def a(var):
  return var**2
print(a(5))