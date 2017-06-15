---
layout: post
title: Increasing Subsequences
date: 2017-06-14
tags:
- Algorithm
categories:
- Array
author: Jason
---
**Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2**

```python
#
# [491] Increasing Subsequences
#
# https://leetcode.com/problems/increasing-subsequences
#
# Medium (38.61%)
# Total Accepted:    8492
# Total Submissions: 21814
# Testcase Example:  '[4,6,7,7]'
#
 
# Example:
# 
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]
# 
# 
# 
# Note:
# 
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be
# considered as a special case of increasing sequence.
#
import copy
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.helper(nums, ret, [], 0)
        return ret

    def helper(self, nums, ret, curr, pos):
        if len(curr) >= 2 and curr not in ret:
            found = copy.deepcopy(curr)
            ret.append(found)
        for index in range(pos, len(nums)):
            if not curr or nums[index] >= curr[-1]:
                curr.append(nums[index])
                self.helper(nums, ret, curr, index + 1)
                del curr[-1]

class Solution(object):
    def findSubsequences(self, nums):
        subs = {()}
        for num in nums:
            subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]
```
