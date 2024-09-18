l = [1,2,2,3,3,3]
set = set(l)
print(set)
l2 = list(set)
print(l2)
dict = {}
for i in l2:
    dict[i] = l.count(i)
print(dict)

