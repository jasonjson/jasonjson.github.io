---
layout: post
title: Power of Three
date: 2016-01-08 16:06:31.000000000 -05:00
tags: algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given an integer, write a function to determine if it is a power of three.</em></strong></p>


``` java
public class Solution {
    public boolean isPowerOfThree(int n) {
        if (n <= 0) return false;
        
        while (n % 3 == 0) {
            n /= 3;
        }
        return n == 1;
    }

    public boolean isPowerOfThree(int n) {
        return (Math.log10(n) / Math.log10(3)) % 1 == 0;
    }
}
```
