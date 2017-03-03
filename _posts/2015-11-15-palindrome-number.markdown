---
layout: post
title: Palindrome Number
date: 2015-11-15 17:33:12.000000000 -05:00
tags: algorithm
categories:
- Integer
author: Jason
---
<p><strong><em>Determine whether an integer is a palindrome. Do this without extra space.</em></strong></p>


``` java
public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int temp = x, rev = 0;
        while (temp != 0) {
            rev = rev * 10 + temp % 10;
            temp /= 10;
        }
        return rev == x;
    }
}
```
