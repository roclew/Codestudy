# 各种list的操作测试
import sys




""""
list_int.append(5)
print(list_int)
print(list_str)

for index in range(len(list_int)):
    print(list_int[index])

for strings in list_int:
    print(strings)

print(list(enumerate(list_int)))
"""

list_int = [x for x in range(100)]
list_str = (x for x in range(100))
print(sys.getsizeof(list_int))
print(sys.getsizeof(list_str))
print(list_int)
for val in list_str:
    print(val)

list1 = [1, 2, 4, 5, 6, 7, 8, 2, 3, 4]
tuple1 = tuple(list1)
set1 = set(list1)
print(tuple1,set1)

