#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.74%)
# Likes:    17532
# Dislikes: 768
# Total Accepted:    1.3M
# Total Submissions: 2.6M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 1. Sort the array
        # 2. Iterate through the array and keep track of the longest consecutive sequence
        # 3. Return the longest consecutive sequence
        # Time complexity: O(nlogn)
        # Space complexity: O(1)

        # nums.sort()
        # longest_streak = 0
        # current_streak = 0

        # for i in range(len(nums)):
        #     if i == 0 or nums[i] != nums[i-1]:
        #         if i > 0 and nums[i] == nums[i-1] + 1:
        #             current_streak += 1
        #         else:
        #             current_streak = 1
        #         longest_streak = max(longest_streak, current_streak)
        # return longest_streak

        # 1. Convert the array into a set of numbers
        # 2. Iterate through the array and check if the current number is the start of the sequence
        # 3. If the current number is the start of the sequence, then check if the next number is in the set
        # 4. If the next number is in the set, then increment the current number and continue
        # 5. If the next number is not in the set, then check if the current sequence is the longest
        # 6. Return the longest consecutive sequence
        # Time complexity: O(n)
        # Space complexity: O(n)

        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)
        return longest_streak

        # 1. Convert the array into a set of numbers
        # 2. Iterate through the array and check if the current number is the start of the sequence
        # 3. If the current number is the start of the sequence, then
# @lc code=end

