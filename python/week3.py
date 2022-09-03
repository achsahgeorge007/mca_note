# def contracting(l):
#     diff= abs(l[1]-l[0])
#     for i in range(2,len(l)):
#         if abs(l[i]-l[i-1])>diff:
#             diff=abs(l[i]-l[i-1])
#         else:
#             return False
#     return True
# print(contracting([9,2,7,3,1]))
# print(contracting([-2,3,7,2,-1]))
# print(contracting([10,7,4,1]))


def contracting(l): 
    for i in range(len(l)-2): 
        if abs(l[i]-l[i+1])>abs(l[i+1]-l[i+2]): 
            continue 
        else: 
            return False 
    return True
print(contracting([11,7,4,2,1]))

def counthv(l):
    hc=0
    vc=0
    for  i in range (1,len(l)-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            hc+=1
        elif l[i]<l[i-1] and l[i]<l[i+1]:
            vc+=1
    return([hc,vc]) 