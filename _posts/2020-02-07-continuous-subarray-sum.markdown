---
layout: post
title: 523 - Continuous Subarray Sum
date: 2020-02-07
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

```python
# [0], 0 -> false;
# [5, 2, 4], 5 -> false;
# [0, 0], 100 -> true;
# [1,5], -6 -> true;
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sums = 0
        sums_dict = {0: -1}
        for i, num in enumerate(nums):
            sums += num
            if k != 0:
                sums = sums % k
            if sums in sums_dict:
                if i - sums_dict[sums] >= 2:
                    return True
            else:
                sums_dict[sums] = i
        return False
```
