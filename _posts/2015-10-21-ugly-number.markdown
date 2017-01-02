---
layout: post
title: Ugly Number
date: 2015-10-21 02:41:36.000000000 -04:00
categories:
- Integer
author: Jason
---
<p><strong><em>Write a program to check whether a given number is an ugly number. Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7. Note that 1 is typically treated as an ugly number.</em></strong></p>


``` java
public class Solution {
    public boolean isUgly(int num) {
        if (num <= 0) return false;
        if (num == 1) return true;
        
        while (num % 5 == 0) {
            num = num / 5;
        }
        
        while (num % 3 == 0) {
            num = num / 3;
        }
        
        while (num % 2 == 0) {
            num = num / 2;
        }
        return num == 1;
    }
}
```
