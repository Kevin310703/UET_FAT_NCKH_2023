# Given an array of integers nums and an integer target, return indices of the two numbers 
# such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the
# same element twice.

nums = [int(x) for x in input().split()]
target = int(input("Type a target number: "))

for i in range (0, len(nums)):
    for j in range (1, len(nums)):
        if int(nums[i]) + int(nums[j]) == target:
            print([i,j])
            quit()

        
