# def gcd(m,n):
#     if m < n:
#         (m,n) =(n,m)

#     if (m%n) == 0:
#         return(n)
#     else:
#         diff = m-n
#         return(gcd(max(n,diff),min(n,diff)))


# def gcd(m,n):
#     if m < n:
#         (m,n) =(n,m)

#     while (m%n) != 0:
#         diff = m-n
#         (m,n) = (max(n,diff),min(n,diff))
#     return(n)      

# def gcd(m,n):
#     if m < n:
#         (m,n) =(n,m)
    
#     while (m%n) != 0:
#         (m,n) = (n,m%n)

#     return(n)

# def h(x):
#     (d,n) = (1,0)
#     while d <= x:
#         (d,n) = (d*3,n+1)
#     return(n)

# print(h(27993))

# def g(n): 
#     s=0
#     for i in range(2,n):
#         if n%i == 0:
#            s = s+1
#     return(s)
# print(g(60)-g(48))

# def f(n): 
#     s=0
#     for i in range(2,n):
#         if n%i == 0:
#            s = s+1
#     return(s)

# print(f(24))


def foo(m):
    if m == 0:
      return(0)
    else:
      return(m+foo(m-1))
print(foo(6))