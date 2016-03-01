N = input("Enter N: ")
M = input("Enter M: ")
l = []
for i in range(N):
    l.append([])
    
for i in range(N):
    for j in range(M):
        l[i].append((i+1)*(j+1))
for i in range(N):
    for j in range(M):
        print l[i][j],
    print 

print 'Sum of rows'
for i in range(0, N):
    sum_row = 0
    for j in range(0, M):
        sum_row += l[i][j]
    print sum_row

print 'Sum of columns'   
for j in range(0, M):
    sum_col = 0
    for i in range(0, N):
        sum_col += l[i][j]
    print sum_col
    
