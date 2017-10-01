---
layout: post
title: Find All Numbers Disappeared in an Array
date: 2017-05-07
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once. Find all the elements of [1, n] inclusive that do not appear in this array. Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.**

```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #For each number i in nums,
        #we mark the number that i points as negative.
        #Then we filter the list, get all the indexes
        #who points to a positive number.
        #Since those indexes are not visited.

        for num in nums:
            i = abs(num) - 1
            nums[i] = -abs(nums[i])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
```
