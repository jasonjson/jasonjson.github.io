---
layout: post
title: 136 - Single Number
date: 2015-10-21 02:33:24.000000000 -04:00
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**Given an array of integers, every element appears twice except for one. Find that single one.**


``` java
public class Solution {
    //利用位运算中的异或：x^x = 0, x^0 = x。并且异或有交换律：1^1^0 = 0 = 1^0^1
    public int singleNumber(int[] A) {
        int result = 0;
        for (int n : A) {
            result ^= n;
        }
        return result;
    }
}
```

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return -1

        xor = 0
        for num in nums:
            xor ^= num
        return xor
```
