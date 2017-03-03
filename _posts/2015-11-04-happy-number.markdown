---
layout: post
title: Happy Number
date: 2015-11-04 15:15:26.000000000 -05:00
tags: algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Write an algorithm to determine if a number is "happy".</p>

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.</em></strong></p>
``` java
public class Solution {
    public boolean isHappy(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10; 
            sum += digit * digit;
            n /= 10;
        }
        if (sum > 9) { 
            return (isHappy(sum));
        } else {
            return sum == 1;
        }
    }
}
```
