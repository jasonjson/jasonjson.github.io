---
layout: post
title: 231 - Power of Two
date: 2015-10-21 02:35:09.000000000 -04:00
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**Given an integer, write a function to determine if it is a power of two.**


``` java
class Solution {
    /*
     * @param n: An integer
     * @return: True or false
     */
    public boolean checkPowerOf2(int n) {
        // write your code here
        if (n < 1 ) return false;
        //n = 0 or n < 0 return false
        //error check !!
        else {
            return ((n & (n - 1)) == 0);
        }
    }
};
```

``` python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        return (n & n - 1) == 0
```
