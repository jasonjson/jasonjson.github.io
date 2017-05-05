---
layout: post
title: Single Number
date: 2015-10-21 02:33:24.000000000 -04:00
tags:
- Algorithm
categories:
- Bit
author: Jason
---
**Given 2n + 1 numbers, every numbers occurs twice except one, find it.**


``` java
public class Solution {
    /**
     *@param A : an integer array
     *return : a integer 
     */
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
        nums.sort()
        i = 0
        while i + 1 < len(nums):
            if nums[i] != nums[i + 1]:
                return nums[i]
            else:
                i += 2
        return nums[-1]
```
