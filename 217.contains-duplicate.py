#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (61.15%)
# Likes:    10187
# Dislikes: 1202
# Total Accepted:    3M
# Total Submissions: 5M
# Testcase Example:  '[1,2,3,1]'
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
#
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#


# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # example input: [1,2,3,1]
        # expected output: true
        # example input 2: [1,2,3,4]
        # expected output 2: false
        # example input 3: [1,1,1,3,3,4,3,2,4,2]
        # expected output 3: true

        # [1, 2, 3, 1]
        # O(n^2)
        # left, right = 0, 1
        # while left < len(nums):
        #     while right < len(nums):
        #         if nums[left] == nums[right]:
        #             return True
        #         else:
        #             right += 1
        #     left += 1
        #     right = left + 1

        # return False

        # O(n)
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # try sorting
        sortedArray = sorted(nums)
        left, right = 0, 1
        while right < len(sortedArray):
            if sortedArray[left] == sortedArray[right]:
                return True
            left += 1
            right += 1
        
        return False


# @lc code=end
