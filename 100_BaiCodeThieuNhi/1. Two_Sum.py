# Given an array of integers, find two numbers such that they add up to a specific target number.

# You may assume that each input would have exactly one solution.

# Input: numbers=[2, 7, 11, 15], target=9 Output: [0,1]

print('Please type an array: ')

arr = [int(a) for a in input().split()] 
target = int(input('type a target number: '))
print(arr)
for i in range(0,len(arr)) :
    for j in range(1,len(arr)) :
        if int(arr[i]) + int(arr[j]) == target :
            print(i,j)