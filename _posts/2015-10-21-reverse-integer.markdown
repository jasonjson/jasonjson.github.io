---
layout: post
title: Reverse Integer
date: 2015-10-21 03:28:44.000000000 -04:00
categories:
- Integer
author: Jason
---
<p><strong><em>Reverse digits of an integer.</em></strong></p>


``` java
public class Solution {
    /**
     * @param n the integer to be reversed
     * @return the reversed integer
     */
    public int reverseInteger(int n) {
        // Write your code here
        if (n > 0) return -reverseInteger(-n);
        
        long result = 0;
        while (n != 0) {
            result = result * 10 + n % 10;
            if (result < Integer.MIN_VALUE) {
                return 0;
            }
            n /= 10;
        }
        return (int) result;
    }
}
```
