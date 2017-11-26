---
layout: post
title: 365 - Count 1 in Binary
date: 2015-10-21 02:38:23.000000000 -04:00
tags:
- Lintcode
categories:
- Bit
author: Jason
---
**Count how many 1 in binary representation of a 32-bit integer.**


``` java
public class Solution {
    /**
     * @param num: an integer
     * @return: an integer, the number of ones in num
     */
    public int countOnes(int num) {
        // write your code here
        int count = 0;
        for (int i = 0; i < 32; i++) {
            if((num & 1) == 1) count ++;
            num >>= 1
        }
        return count;
    }
}
```

``` python
class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here
        count = 0
        for _ in xrange(32):
            if num & 1 == 1:
                count += 1
            num >>= 1
        return count
```
