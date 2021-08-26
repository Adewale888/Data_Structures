
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


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=strs
        
        xx= len(strs[0])
        for i in x:
            if len(i) < xx:
                xx= len(i)
        print(xx)
            
        result=""
        word = x[0][0:xx]
        
        print(word)
        for i in range (xx):
            for j in range (len(x)):
                if x[j][i] != word[i]:
                    return result
                 
            result += word[i]
                    
        return result