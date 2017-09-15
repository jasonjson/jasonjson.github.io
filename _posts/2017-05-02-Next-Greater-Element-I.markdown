---
layout: post
title: Next Greater Element I
date: 2017-05-02
tags:
- Algorithm
categories:
- Array
author: Jason
---
**You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2. The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.**

```python
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        #map里保存着findNums里每个数的next greater element
        next_greater_map = {}
        #stack里面的数字是降序排列，例如5，4，6当处理到6时
        #stack里有5，4，两者的next greater element都是6
        stack = []
        ret = []
        for num in nums:
            while stack and stack[-1] < num:
                next_greater_map[stack.pop()] = num
            stack.append(num)

        for num in findNums:
            ret.append(next_greater_map.get(num, -1))

        return ret
```
