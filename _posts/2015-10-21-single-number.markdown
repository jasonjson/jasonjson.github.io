---
layout: post
title: Single Number
date: 2015-10-21 02:33:24.000000000 -04:00
categories:
- Bit
author: Jason
---
<p><strong><em>Given 2n + 1 numbers, every numbers occurs twice except one, find it.</em></strong><br />


``` java
public class Solution {
    /**
     *@param A : an integer array
     *return : a integer 
     */
    public int singleNumber(int[] A) {
        int result = 0;
        for (int n : A) {
            result ^= n;
        }
        return result;
    }
}
```
