x = {1,2,3,4,5,6}
y = {1,2,3,8,9,0}
x1 = {1,2,3}
print(x & y) # intersection
print(x | y) # union
print(x - y) # difference
print(x ^ y) # symmetric difference
print(x1.issubset(x))
print(x.issubset(x1))
print(x.issuperset(x1))