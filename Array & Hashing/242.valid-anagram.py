#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (63.06%)
# Likes:    9992
# Dislikes: 319
# Total Accepted:    2.4M
# Total Submissions: 3.8M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# O(n) time complexity = O(s + t)

# @lc code=start
# 1)
# class Solution(object):
#     def isAnagram(self, s, t):
#         return Counter(s) == Counter(t)

# try doing it with O(1) space complexity

# 2) 
class Solution(object):
    def isAnagram (self, s, t):
        return sorted(s) == sorted(t)

# 3)
# class Solution(object):
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False
        
#         s_dict = {}
#         t_dict = {}

#         for i in range(len(s)):
#             if s[i] not in s_dict:
#                 s_dict[s[i]] = 1
#             else:
#                 s_dict[s[i]] += 1

#             if t[i] not in t_dict:
#                 t_dict[t[i]] = 1
#             else:
#                 t_dict[t[i]] += 1

#         for key in s_dict:
#             if key not in t_dict or s_dict[key] != t_dict[key]:
#                 return False

#         return True
# @lc code=end

