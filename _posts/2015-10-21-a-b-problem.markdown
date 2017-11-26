---
layout: post
title: 1 - A + B Problem
date: 2015-10-21 02:39:12.000000000 -04:00
tags:
- Lintcode
categories:
- Bit
author: Jason
---
**Write a function that add two numbers A and B. You should not use + or any arithmetic operators.**


``` java
class Solution {
    /*
     * param a: The first integer
     * param b: The second integer
     * return: The sum of a and b
     */
    public int aplusb(int a, int b) {
        // write your code here, try to do it without arithmetic operators.
        int result = a ^ b;
        int carry = a & b;
        carry <<= 1;
        if (carry != 0) {
            result = aplusb(result, carry);
        }
        return result;
    }
};
```

``` python
class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        #^y //执行加法，不考虑进位。
        #(x&y)<<1 //进位操作
        if b == 0:
            return a

        summation = a ^ b
        carry = (a & b) << 1
        return self.aplusb(summation, carry)
```
