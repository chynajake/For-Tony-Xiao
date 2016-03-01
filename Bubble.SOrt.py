## BUBBLE SORT
nums = [1, 5, 2, 9, 95, 6, 7, 3, 1, 4]

swapped = True # make a flag

while swapped:
    swapped = False
    for i in xrange(len(nums)-1):
        if nums[i]>nums[i+1]:
            swapped = True
            nums[i],nums[i+1] = nums[i+1],nums[i]
            print nums
