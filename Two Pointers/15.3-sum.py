#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (32.99%)
# Likes:    27645
# Dislikes: 2485
# Total Accepted:    2.8M
# Total Submissions: 8.6M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
#
#
# Example 2:
#
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
# Example 3:
#
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#


# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # time complexity: O(n^2)
        # space complexity: O(1) || O(n) if we consider the space required for the output

        # example: [-1,0,1,2,-1,-4]
        nums.sort()
        # example: [-4, -1, -1, 0, 1, 2]
        # remove duplicates
        # example: [-4, -1, 0, 1, 2]
        result = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        
        # result: [[-1, -1, 2], [-1, 0, 1]]
        return result

        # nums.sort()
        # result = []
        # for i in range(len(nums)-2):
        #     if i == 0 or nums[i] != nums[i-1]:
        #         left = i+1
        #         right = len(nums)-1
        #         while left < right:
        #             total = nums[i] + nums[left] + nums[right]
        #             if total < 0:
        #                 left += 1
        #             elif total > 0:
        #                 right -= 1
        #             else:
        #                 result.append([nums[i], nums[left], nums[right]])
        #                 while left < right and nums[left] == nums[left+1]:
        #                     left += 1
        #                 while left < right and nums[right] == nums[right-1]:
        #                     right -= 1
        #                 left += 1
        #                 right -= 1

        # return result


# @lc code=end
