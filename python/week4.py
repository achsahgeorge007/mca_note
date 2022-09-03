# def mystery(l):
#     if l == []:
#         return(l)
#     else:
#         return(mystery(l[1:])+l[:1])
# print(mystery([22,14,19,65,82,55]))

# def frequency(l):
#     unique_l = list(set(l))
#     freq_list = [l.count(x) for x in unique_l]
#     min_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == min(freq_list)]
#     max_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == max(freq_list)]
#     min_freq_list.sort()
#     max_freq_list.sort()
#     return (min_freq_list, max_freq_list)
# print(frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7]))

def onehop(lst):
    data = lst
    data.sort(key=lambda tup: tup[0])
    ans = []
    for ele in lst:
        x, y = ele
        for ele1 in lst:
            if ele != ele1:
                xx, yy = ele1
                if y == xx and x != yy and (x,yy) not in ans:
                    ans.append((x, yy))
    ans = sorted(ans, key=lambda tup: (tup[0], tup[1]))
    return ans
print(onehop([(1,2),(3,4),(5,6)]))