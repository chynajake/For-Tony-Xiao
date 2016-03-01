N = input('Write N: ')
i = 1
a = 0
while i <= N:
    if N % i == 0:
        a = a + 1
    elif N % i == 1:
        a = a + 0
    else:
        a = a + 0
    i = i + 1
if a > 2:
    print 'Number ' ,N, ' is not prime number'
elif a == 2:
    print 'Number ' ,N, ' is prime number'
else:
    print 'Number ' ,N, ' is 1'
