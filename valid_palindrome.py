"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string1 = ""
        for i in s:
            if i.isalpha():
                string1 += i.lower()
            elif i.isnumeric():
                string1 += i
                
        ini = 0
        last = len(string1)  - 1
        while ini <= last:
            if string1[ini] != string1[last]:
                return False
            else:
                ini += 1
                last -= 1
        return True