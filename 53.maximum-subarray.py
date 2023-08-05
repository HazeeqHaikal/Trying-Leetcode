#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Medium (50.27%)
# Likes:    31082
# Dislikes: 1322
# Total Accepted:    3.3M
# Total Submissions: 6.6M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the subarray with the largest sum, and
# return its sum.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# 
# 
# Example 3:
# 
# 
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
# 
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        >>> s = Solution()
        >>> s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> s.maxSubArray([1])
        1
        >>> s.maxSubArray([5,4,-1,7,8])
        23
        """
        # time complexity = O(n)
        # remove negative prefix
        max_sum = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum < 0:
                current_sum = 0
            max_sum = max(max_sum, current_sum)
        if max_sum == 0:
            return max(nums)
        return max_sum

        # max_sum = nums[0]
        # current_sum = 0
        # for num in nums:
        #     if current_sum < 0:
        #         current_sum = 0
        #     current_sum += num
        #     max_sum = max(max_sum, current_sum)
        # return max_sum
    
        
# @lc code=end

