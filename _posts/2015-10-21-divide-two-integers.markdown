---
layout: post
title: Divide Two Integers
date: 2015-10-21 14:04:10.000000000 -04:00
tags:
- Algorithm
categories:
- Integer
author: Jason
---
**Divide two integers without using multiplication, division and mod operator. If it is overflow, return 2147483647**


``` java
public class Solution {
    /**
     * @param dividend the dividend
     * @param divisor the divisor
     * @return the result
     */
    public int divide(int dividend, int divisor) {
        // Write your code here
        boolean positive = true;
        if ((dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0)) {
            positive = false;
        }
        long dvd = Math.abs((long)dividend);//先转化成long再求绝对值
        long dvs = Math.abs((long)divisor);

        long result = helper(dvd, dvs);
        if (result >= Integer.MAX_VALUE) {
            return positive ? Integer.MAX_VALUE : Integer.MIN_VALUE;
        }
        return positive ? (int) result : -(int)result;
    }

    public long helper(long dvd, long dvs) {
        if (dvd < dvs) return 0;
        long sum = dvs, multiple = 1;
        while (sum + sum <= dvd) {
            sum += sum;
            multiple += multiple;
        }
        return multiple + helper(dvd - sum, dvs);
    }
}
```

``` python
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        positive = (dividend < 0) is (divisor < 0)
        dvd, dvs = abs(dividend), abs(divisor)
        ret = 0
        while dvd >= dvs:
            tmp, multiple = dvs, 1
            while dvd >= tmp:
                dvd -= tmp
                ret += multiple
                multiple <<= 1
                tmp <<= 1
        if not positive:
            ret = -ret
        return min(max(-2 ** 31, ret), 2 ** 31 - 1)
```
