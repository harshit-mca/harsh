a={1,2,3,4,5,6,1,2,3,7,8,9,10}
b={1,2,3,4}
c={6,7,8,9,10}
d={3,4,5,6,7,8}
e={11,22,33}


e.add('apple')
c.remove(9)
d.update([1,2,3,56,77,8,3,9])
e.pop()

print(a)
print(b)
print(c)
print(d)
print(e)

print(a.issuperset(c),'a is superset of c')
print(a.issuperset(d),'a is superset of d')

if b.issubset(a):
    print("b is subset of a")
else:
    print('b is not subset of a')
if e.issubset(d):
    print("e is subset of d")
else:
    print('e is not subset of d')

if a.isdisjoint(e):
    print("a and e me koi rista nhi")
else:
    print('a and e are connected')

if b.isdisjoint(d):
    print("b and d me koi rista nhi")
else:
    print('b and d are connected')

print('union')
print(a.union(d))
print(a|d)

print('difference')
print(a.difference(d))
print(a-d)

print('intersection')
print(a.intersection(d))
print(a&d)

print('symmetric difference')
print(a.symmetric_difference(d))
print(a^d)