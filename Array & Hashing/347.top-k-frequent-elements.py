#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.48%)
# Likes:    15456
# Dislikes: 542
# Total Accepted:    1.6M
# Total Submissions: 2.5M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#

# @lc code=start
from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # example: [1,1,1,2,2,3], k = 2
        # output: [1,2]
        # time complexity: O(nlogn)
        frequent = defaultdict(int)
        for n in nums:
            frequent[n] += 1

        # frequent: {1: 3, 2: 2, 3: 1}
        sorted_frequent = sorted(frequent.items(), key=lambda x: x[1], reverse=True)
        # sorted_frequent: [(1, 3), (2, 2), (3, 1)]
        res = []
        for i in range(k):
            res.append(sorted_frequent[i][0])

        return res

        # time complexity: O(n)
        # count = {}
        # frequent = [[] for i in range(len(nums) + 1)]
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # for n, c in count.items():
        #     frequent[c].append(n)

        # res = []
        # for i in range(len(frequent) - 1, 0, -1):
        #     for n in frequent[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res


# @lc code=end
