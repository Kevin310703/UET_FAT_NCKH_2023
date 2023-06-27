"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

"""


print('Please type an arr: ')

arr = [int(a) for a in input().split()]
target = int(input('type a target number: '))

for i in range(0, len(arr)) :
    if int(arr[i]) == target :
        print(i)
    else :
        print('Please type another target number next time.')
        quit()
