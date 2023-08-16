a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])

print(a)
print(b)

print(a & b)    # 交集
print(a | b)    # 并集
print(a - b)    # 差集
print(a ^ b)    # 双差集

print(a.union(b))   # 交集
print(a.intersection(b))    # 并集
print(a.difference(b))  # 差集
print(a.symmetric_difference(b))


a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])
a.update(b)
print(a)

a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])
a.intersection_update(b)
print(a)

a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])
a.difference_update(b)
print(a)
