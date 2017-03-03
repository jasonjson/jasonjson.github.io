---
layout: post
title: Convert Integer A to Integer B
date: 2015-10-21 02:35:52.000000000 -04:00
tags: algorithm
categories:
- Bit
author: Jason
---
<p><strong><em>Determine the number of bits required to convert integer A to integer B Example: Given n = 31, m = 14,return 2</em></strong></p>


``` java
public class Solution {
    public static int convert2(int a, int b) {
        int xor = a ^ b;
        int number = 32, count = 0;
        while (number > 0) {
            if ((xor & 1) == 1) {
                count ++;
            }
            number --;
            xor >>= 1;
        }
        return count;
    }
}
```
