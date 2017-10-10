---
layout: post
title: 190 - Reverse Bits
date: 2015-11-04 16:16:49.000000000 -05:00
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**Reverse bits of a given 32 bits unsigned integer.**


``` java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            if (((n >> i) & 1) == 1) {
                result |= 1 << (31 - i);
            }
        }
        return result;
    }
}
```

``` python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in xrange(32):
            if (n >> i) & 1:
                ret |= 1 << (31 - i)
        return ret
```
