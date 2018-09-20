---
layout: post
title: 171 - Excel Sheet Column Number
date: 2015-11-05 11:50:50.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a column title as appear in an Excel sheet, return its corresponding column number.**


``` java
public class Solution {
    public int titleToNumber(String s) {
        if (s == null || s.length() == 0) return 0;
        int result = 0;
        for (char c : s.toCharArray()) {
            result = result * 26 + (int)(c - 'A' + 1);
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        ret = 0
        for c in s:
            ret = ret * 26 + ord(c) - ord("A") + 1
        return ret
```
