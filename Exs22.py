n = int(input())
m = int(input())
set_1 = set()
set_2 = set()
set_result = set()
for i in range(n):
    x = int(input())
    set_1.add(x)
for i in range(m):
    x = int(input())
    set_2.add(x)
set_result = set_1.intersection(set_2)
list_1 = list(set_result)
list_1.sort()
for i in list_1:
    print(i, end=' ')