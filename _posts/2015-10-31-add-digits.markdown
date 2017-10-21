---
layout: post
title: 258 - Add Digits
date: 2015-10-31 10:40:28.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a non-negative integer num, repeatedly add all its digits until the result has only one digit. For example: Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.**


``` java
public class Solution {
    public int addDigits(int num) {
        if (num == 0) return 0;
        return num % 9 == 0 ? 9 : num % 9;//观察结果 与9相关
    }
}
public class Solution {
    public int addDigits(int num) {
        String s = String.valueOf(num);
        while (s.length() > 1) {
            int sum = 0;
            for (char c : s.toCharArray()) {
                sum += Character.getNumericValue(c);
            }
            s = String.valueOf(sum);
        }
        return Integer.parseInt(s);
    }
}
```

``` python
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0
        return 9 if num % 9 == 0 else num % 9
```
