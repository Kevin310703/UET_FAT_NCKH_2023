# Given an array of integers, find two numbers such that they add up to a specific target number.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9 Output: index1=1, index2=2
print("Please type an array of integers: ")
nums = [int(x) for x in input().split()]
target = int(input("Type a target number: "))

for i in range (0, len(nums)):
    for j in range (1, len(nums)):
        if int(nums[i]) + int(nums[j]) == target:
            print([i,j])

