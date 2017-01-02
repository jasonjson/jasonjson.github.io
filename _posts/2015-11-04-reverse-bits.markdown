---
layout: post
title: Reverse Bits
date: 2015-11-04 16:16:49.000000000 -05:00
categories:
- Bit
author: Jason
---
<p><strong><em>Reverse bits of a given 32 bits unsigned integer.</em></strong></p>

``` java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            if (((n >>> i) & 1) == 1) {
                result |= 1 << (31 - i);
            }
        }
        return result;
    }
}
```
