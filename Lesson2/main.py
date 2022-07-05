#Задача 1
num = input().split()
a = []
for i in range(1, len(num)):
    if i % 3 == 0 and i % 5 != 0:
        a.append(int(i))
print(min(a), max(a))
print(a[0], a[-1])

#Задача 2
num = input().split()
a = []
for i in num:
    if num.count(i) == 1:
        a.append(i)
print(a)