##COUNTING SORT


count = {}
for i in num:
    count[i] = count.get(i, 0) + 1

for x in range(101):
    for n in range(count.get(x,0)):
        print x
