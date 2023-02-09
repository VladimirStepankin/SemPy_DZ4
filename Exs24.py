n = int(input())
list_1 = list()
for i in range(n):
    list_1.append(int(input()))
summ_max = 0
summ = 0
for i in range(n):
    summ = sum(list_1[i:i+3])
    if summ > summ_max:
        summ_max = summ
if list_1[0] + list_1[-1] + list_1[-2] > summ_max:
    summ_max = list_1[0] + list_1[-1] + list_1[-2]
if list_1[0] + list_1[1] + list_1[-1] > summ_max:
    summ_max = list_1[0] + list_1[1] + list_1[-1]
print(summ_max)
