''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

  You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for each number in the list, pick one append index to output list 
        #check if itterate through other numbers and check addition
        # if match add the other number index to output list
        # if not match replace with second number index and do the same      
        store = {}
        out = []
        for i,n in enumerate (nums):
            print (i)
            print (n)
            if target - n in store:
                return [i, store[target - n]]
                print(store.values())
            store[n] = i
        return out



        
