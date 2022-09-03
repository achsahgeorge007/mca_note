# x = [[3,5],"mimsy",2,"borogove",1]
# y = x[0:50]                         
# z = y                               
# w = x                               
# x[1] = x[1][:5] + 'ery'             
# y[1] = 4                             
# w[1][:3] = 'fea'                     
# z[4] = 42                            
# x[0][0] = 5555                       
# a = (x[3][1] == 1)                   

# b = [43,99,65,105,4]
# a = b[2:]
# d = b[1:]
# c = b
# d[1] = 95
# b[2] = 47
# c[3] = 73

# print(a,b,c,d)

# startmsg = "anaconda"
# endmsg = ""
# for i in range(1,1+len(startmsg)):
#   endmsg = endmsg + startmsg[-i]

# print(endmsg)

# def mystery(l):
#   l = l[2:]
#   return(l)
# mylist = [7,11,13,17,19,21]
# mystery(mylist)
# print(mystery(mylist))
# print(mylist)

# import math
# x = math.sqrt(9)
# print(x)

# i = 10
# j = 3
# print(j)
# print(i==10 or i%j == 0)

# def divides(m,n):
#   if n%m == 0:
#     return(True)
#   else:
#     return(False)

# def even(n):
#   return(divides(2,n))

# def odd(n):
#   return(not divides(2,n))
# print(odd(16))

# title="India's 76th Independence day is celebrated in Aug 15 2022"
# print(title)

# hname = "Shibin"
# wname = "Achsah"

# print(name[-3])
# print("My name is" + " " + name)
# print(len(name))
# print(hname[:3] + wname[3:])

# nested = [["Hai", "Hello"],7,["Welcome"]]
# print(nested[0][0][2])
# nested[1] = 1
# print(nested)

# list1 = [1,2,3,4]
# list2 = list1[:]
# list1[2] = 4
# print(list1)
# print(list2)

# list1 = [1,2,3,4]
# list2 = [1,2,3,4]
# list2 = [5,6,7,8]
# list3 = list2
# print(list1 == list2)
# print(list2 == list3)
# print(list1 is list2)
# print(list2 is list3)
# print(list1 + list2)
# print(list1 + [10])

# def Person(age):
#   if age > 18:
#     return("Major Indian citizen")
#   else:
#     return("Minor Citizen")
# print(Person(15))

# def power(x,n):
#   ans = 1
#   for i in range(0,n):
#     ans = ans*x
#   return(ans)
# print(power(5,4))

# def stupid(x):
#   n=17
#   return(x)
# n=7
# v=stupid(28)
# print(n)

# def f(x):
#   return g(x+1)
# def g(y):
#   return(y+3)
# z = f(77)
# print(f(z))

# num = 1234
# reversed_num = 0
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
# print("Reversed Number: " + str(reversed_num))

# n = 23456
# reverse = 0
# while(n > 0):
#     reminder = n%10
#     reverse = reverse*10 + reminder
#     n = n//10
# print(reverse)

# Number = int(input("Please Enter any Number: "))    
# Reverse = 0    
# while(Number > 0):    
#     Reminder = Number %10    
#     Reverse = (Reverse *10) + Reminder    
#     Number = Number //10    
     
# print("\n Reverse of entered number is = %d" %Reverse)

# def intreverse(n):
#   reverse = 0
#   remainder = 0

#   while(n != 0):
#     remainder = n % 10
#     reverse = reverse * 10 + remainder
#     n = int(n / 10)
#   return reverse

# print(intreverse(6789))
# Test Case 1
#print(intreverse(368))

# Test Case 2
#print(intreverse(798798))

# Test Case 3
#print(intreverse(7))

# def matched(s):
#   bracketCounter = 0
#   i = 0
#   while bracketCounter >=0 and i<len(s):
#     if s[i] == "(":
#       bracketCounter += 1
#     elif s[i] == ")":
#       bracketCounter -= 1
#     i += 1
  
#   if bracketCounter == 0:
#     return True
#   else:
#     return False

# print(matched("Hai i am Achsah"))

def sumprimes(l):
    primeNum = []
    for item in l:
        is_prime = True
        if(item >= 2):
            maxInt = int(item ** 0.5) + 1
            for i in range(2, maxInt):
                if(item % i == 0):
                    is_prime = False
                    break
            if(is_prime):
                primeNum.append(item)
    return(sum(primeNum))

print(sumprimes([17,51,29,39]))
print(sumprimes([-3,-5,3,5]))
print(sumprimes([4,6,15,27]))
