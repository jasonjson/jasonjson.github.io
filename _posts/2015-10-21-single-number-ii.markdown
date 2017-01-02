---
layout: post
title: Single Number II
date: 2015-10-21 02:34:03.000000000 -04:00
categories:
- Bit
author: Jason
---
<p><strong><em>Given 3n + 1 numbers, every numbers occurs triple times except one, find it.</em></strong></p>


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
