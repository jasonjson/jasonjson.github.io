---
layout: post
title: Matchsticks To Square
date: 2017-06-14
tags:
- Algorithm
categories:
- DFS BACKTRACKING
author: Jason
---
**Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.⁠Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.**

```python
#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square
#
# Medium (34.55%)
# Total Accepted:    8109
# Total Submissions: 23454
# Testcase Example:  '[1,1,2,2,2]'
#
 
# Example 1:
# 
# Input: [1,1,2,2,2]
# Output: true
# 
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
# 
# 
# 
# Example 2:
# 
# Input: [3,3,3,3,4]
# Output: false
# 
# Explanation: You cannot find a way to form a square with all the
# matchsticks.

class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)
        if not nums or total % 4 != 0:
            return False
        nums.sort(reverse=True)
        return self.helper(nums, 0, [0] * 4, total / 4)

    def helper(self, nums, index, sums, length):
        if index == len(nums):
            return True

        for i in range(4):
            if sums[i] + nums[index] > length:
                continue
            sums[i] += nums[index]
            if self.helper(nums, index + 1, sums, length):
                return True
            sums[i] -= nums[index]

        return False




```
