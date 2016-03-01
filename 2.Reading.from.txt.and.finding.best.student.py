import random
input = open("marks.txt", "r")
n = input.readline()
max = 0
name = ""
for i in range(int(n)):
    l = input.readline().split()
    sum = 0
    for j in range(1, 4):
        sum += int(l[j])
        average = sum / 3
        if average > max:
            max = average
            name = l[0]
            marks = l[1:4]
print max
print name
print marks
print "THE BEST IS: "+name+" with marks: "+str(marks)   
        
