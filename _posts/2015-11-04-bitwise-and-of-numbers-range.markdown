---
layout: post
title: Bitwise AND of Numbers Range
date: 2015-11-04 15:36:13.000000000 -05:00
categories:
- Bit
- Brain teaser
author: Jason
---
<p><strong><em>Given a range [m, n] where 0 &lt;= m &lt;= n &lt;= 2147483647, return the bitwise AND of all numbers in this range, inclusive.<br />

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
