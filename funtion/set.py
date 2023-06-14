s1 = set([1,2,3])
print(s1)

s2 = set("hello")
print(s2)

s1.add(4)
print(s1)
s1.update([4,5,6])
print(s1)
s1.remove(1)
print(s1)

l1 = list(s1)
l2 = tuple(s1)
print(l1)
print(l2)