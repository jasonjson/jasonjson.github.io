---
layout: post
title: Largest Divisible Subset
date: 2017-09-12
tags:
- Algorithm
categories:
- Array
author: Jason
---
**Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0. If there are multiple solutions, return any subset is fine.**

```python
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset
#
# Medium (33.63%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3]'
#
import copy
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in reversed(range(0, i)):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    break

        max_subset_index = dp.index(max(dp))
        subset_size = dp[max_subset_index]
        to_add = nums[max_subset_index]
        ret = []
        for i in reversed(range(max_subset_index + 1)):
            if to_add % nums[i] == 0 and dp[i] == subset_size:
                ret.append(nums[i])
                to_add = nums[i]
                subset_size -= 1

        return ret

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.largestDivisibleSubset([2,3,8,9,27]))

```
