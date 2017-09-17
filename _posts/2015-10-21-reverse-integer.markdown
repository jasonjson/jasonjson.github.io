---
layout: post
title: Reverse Integer
date: 2015-10-21 03:28:44.000000000 -04:00
tags:
- Algorithm
categories:
- Integer
author: Jason
---
**Reverse digits of an integer.**


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

```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            return -self.reverse(-x)
        ret = 0
        while x:
            ret = ret * 10 + x % 10
            x /= 10
        #-10 % 3 = 2,i does not work well with python

        return ret if ret < 2 ** 31 else 0
```
