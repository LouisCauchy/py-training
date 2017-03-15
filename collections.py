x = {1,2,3,4,5,6}
y = {1,2,3,8,9,0}
x1 = {1,2,3}
d1 = dict({"id": 1948, "name": "Washer", "size": 3})
d2 = dict(id=1948, name="Washer", size=3)
d3 = dict([("id", 1948), ("name", "Washer"), ("size", 3)])
d4 = dict(zip(("id", "name", "size"), (1948, "Washer", 3)))
d5 = {"id": 1948, "name": "Washer", "size": 3}
print(d1,d2,d3,d4,d5)
print(x & y) # intersection
print(x | y) # union
print(x - y) # difference
print(x ^ y) # symmetric difference
print(x1.issubset(x))
print(x.issubset(x1))
print(x.issuperset(x1))
for value in d1.values():
	print(value)