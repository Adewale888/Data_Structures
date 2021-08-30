"""
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ini=0
        last= len (nums)-1
        count = 0
        #for i in range ((last)-1):
        if target < nums[ini]:
            return 0 
        
        while ini <= last:
            if nums[ini] == target:
                return ini
            
            elif nums[ini] < target:
                ini += 1
                
                
            elif nums[ini] > target:
                return ini
        return ini
                