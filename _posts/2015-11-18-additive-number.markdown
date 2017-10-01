---
layout: post
title: Additive Number
date: 2015-11-18 09:31:17.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>Additive number is a positive integer whose digits can form additive sequence.</p>

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.</em></strong></p>
``` java
import java.math.BigInteger;
public class Solution {
    public boolean isAdditiveNumber(String num) {
        if (num == null || num.length() < 3) return false;
        
        for (int i = 1; i <= num.length() / 2; i++) {
            if (num.charAt(0) == '0' && i > 1) break;//0 is the starting point of the first number
            BigInteger a = new BigInteger(num.substring(0, i));
            for (int j = 1; Math.max(i, j) <= num.length() - i - j; j++) {
                if (num.charAt(i) == '0' && j > 1) break;//i is the starting point of the second number
                BigInteger b = new BigInteger(num.substring(i, i + j));
                if (isValid(num.substring(i + j), a, b)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    public boolean isValid(String num, BigInteger a, BigInteger b) {
        if (num.length() == 0) return true;
        
        b = a.add(b);
        a = b.subtract(a);
        String c = String.valueOf(b);
        return num.startsWith(c) && isValid(num.substring(c.length()), a, b);
    }
}
```
