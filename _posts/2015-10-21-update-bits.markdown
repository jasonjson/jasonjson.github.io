---
layout: post
title: Update Bits
date: 2015-10-21 02:37:14.000000000 -04:00
tags:
- Algorithm
categories:
- Bit
author: Jason
---
<p><strong><em>Given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N equal to M (eg , M becomes a substring of N located at i and starting at j)</em></strong></p>


``` java
class Solution {
    /**
     *@param n, m: Two integer
     *@param i, j: Two bit positions
     *return: An integer
     */
    public int updateBits(int n, int m, int i, int j) {
        // write your code here
        //first step : clear bits in N from i to j
        int mask = 0;
        if (j < 31) {
            //when j gets to 31, the leftmost digit (right part starts from 0)
            //is automatically cleared, we only need to find right portion
            //In other words, we don't need to add 1s to the left part
            //ones = ~0 
            //zeroes = 0
            mask = (~0 << (j + 1)) | ((1 << i) - 1);
        } else {
            mask = (1 << i) - 1;
        }
        return ((n & mask) | (m << i));
    }
}
```
