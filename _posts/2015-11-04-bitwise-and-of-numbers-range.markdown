---
layout: post
title: 201 - Bitwise AND of Numbers Range
date: 2015-11-04 15:36:13.000000000 -05:00
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.**

For example, given the range [5, 7], you should return 4.</em></strong></p>
``` java
public class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        int diffDigits = 0;
        while (m != n) {
            m >>= 1;
            n >>= 1;
            diffDigits ++;
        }
        return n << diffDigits;
    }//Find the same prefix of the numbers in this range.
}
```

``` python
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        diff = 0
        while m != n:
            m >>= 1
            n >>= 1
            diff += 1
        return m << diff
```
