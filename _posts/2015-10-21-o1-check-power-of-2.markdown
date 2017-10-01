---
layout: post
title: O(1) Check Power of 2
date: 2015-10-21 02:35:09.000000000 -04:00
tags:
- Leetcode
categories:
- Bit
author: Jason
---
<p><strong><em>Using O(1) time to check whether an integer n is a power of 2.</em></strong></p>


``` java
class Solution {
    /*
     * @param n: An integer
     * @return: True or false
     */
    public boolean checkPowerOf2(int n) {
        // write your code here
        if (n < 1 ) return false;
        //n = 0 or n < 0 return false
        //error check !!
        else {
            return ((n & (n - 1)) == 0);
        }
    }
};
```
