---
layout: post
title: 689 - Maximum Sum Of 3 Non Overlapping Subarrays
date: 2020-02-07
tags:
- Leetcode
categories:
- Array
author: Jason
---
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum. Each subarray will be of size k, and we want to maximize the sum of all 3*k entries. Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

```python
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 3 * k:
            return []

        s1, s2, s3 = sum(nums[:k]), sum(nums[k: 2*k]), sum(nums[2*k: 3*k])
        index1, index2, index3 = [0], [0, k], [0, k, 2*k]
        t1, t2, t3 = s1, s1 + s2, s1 + s2 + s3

        for i in range(1, len(nums) - 3 * k + 1):
            s1 += nums[i + k - 1] - nums[i - 1]
            s2 += nums[i + 2 * k - 1] - nums[i + k - 1]
            s3 += nums[i + 3 * k - 1] - nums[i + 2 * k - 1]
            if s1 > t1:
                t1, index1 = s1, [i]
            if t1 + s2 > t2:
                t2, index2 = t1 + s2, index1 + [i + k]
            if t2 + s3 > t3:
                t3, index3 = t2 + s3, index2 + [i + 2 * k]
        return index3
```
