---
layout: post
title: 168 - Excel Sheet Column Title
date: 2015-11-05 11:43:27.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a positive integer, return its corresponding column title as appear in an Excel sheet.**


``` java
public class Solution {
    public String convertToTitle(int n) {
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            int digit = n % 26;
            n /= 26;
            if (digit == 0) {//deal with 26 separately
                sb.append("Z");
                n --;
            } else {
                sb.append((char)(digit - 1 + 'A'));
            }
        }
        return sb.reverse().toString();
    }
}
```

``` python
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        ret = []
        while n:
            n -= 1
            ret.append(chr(n % 26 + ord("A")))
            n //= 26
        return "".join(reversed(ret))
```
