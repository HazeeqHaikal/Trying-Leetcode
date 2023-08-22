#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (65.07%)
# Likes:    19102
# Dislikes: 1067
# Total Accepted:    1.8M
# Total Submissions: 2.8M
# Testcase Example:  '[1,2,3,4]'
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
#
#
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
#
#

# @lc code=start
from collections import defaultdict


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # time complexity: O(n)
        prefix = []
        postfix = []
        res = []

        totalPre, totalPost = 1, 1
        lastIndex = len(nums)

        for i in range(0, lastIndex):
            totalPre *= nums[i]
            prefix.append(totalPre)

            totalPost *= nums[lastIndex - 1 - i]
            postfix.append(totalPost)

        for i in range(0, lastIndex):
            if i == 0:
                res.append(postfix[lastIndex - 2])
            elif i == lastIndex - 1:
                res.append(prefix[lastIndex - 2])
            else:
                res.append(prefix[i - 1] * postfix[lastIndex - 2 - i])

            # if left == 0:
            #     res.append(postfix[right])
            # elif right == lastIndex - 1:
            #     res.append(prefix[left - 1])
            # else:
            #     res.append(prefix[left - 1] * postfix[right])

        return res


# @lc code=end
