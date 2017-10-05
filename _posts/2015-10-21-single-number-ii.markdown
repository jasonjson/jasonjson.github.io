---
layout: post
title: 137 - Single Number II
date: 2015-10-21 02:34:03.000000000 -04:00
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**Given 3n + 1 numbers, every numbers occurs triple times except one, find it.**


``` java
public class Solution {
    public int singleNumber(int[] nums) {
        if (nums == null || nums.length == 0) return -1;

        int[] digits = new int[32];
        int result = 0;
        for (int i = 0; i < 32; i++) {
            for (int j = 0; j < nums.length; j++) {
                digits[i] += (nums[j] >> i) & 1;
            }
            result |= digits[i] % 3 << i;
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return -1
        ret = 0
        for i in xrange(32):
            digit = 0
            for num in nums:
                digit += (num >> i) & 1
            ret |= (digit % 3) << i
        return ret - 2 ** 32 if ret >= 2 ** 31 else ret
```
