"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    
Explanation: There is no common prefix among the input strings.

"""

def longestCommonPrefix(strs):
    
    if not strs:
        return ""

    
    chuoi_min = min(len(s) for s in strs)

   
    for i in range(chuoi_min):
        
        char = strs[0][i]

        
        if not all(s[i] == char for s in strs):
           
            return strs[0][:i]

    
    return strs[0][:chuoi_min]



a = str(input('Nhap chuoi :'))
print(longestCommonPrefix(a))

#cíu em em o biết sai ở đâu, mắc kẹt ở đây từ chiều :))))