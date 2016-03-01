## LINEAR SEARCH

nums = [1, 5, 2, 9, 95, 6, 7, 3, 1, 4]
seeking_value = 4
marker = True
for i in nums:
    if i == seeking_value:
        print i, "index is", nums.index(i)
        marker = False
if marker:
    print "NO SUCH VALUE"
