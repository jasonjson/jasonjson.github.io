---
layout: post
title: 8 - String to Integer(atoi)
date: 2015-10-21 13:23:18.000000000 -04:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Implement function atoi to convert a string to an integer. If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.**


``` java
public class Solution {
    /**
     * @param str: A string
     * @return An integer
     */
    public int atoi(String str) {
        // write your code here
        if (str == null || str.length() == 0) return 0;

        str = str.trim();
        long result = 0;
        int index = 0, sign = 1;
        if (str.charAt(index) == '+') {
            index ++;
        } else if (str.charAt(index) == '-') {
            sign = -1;
            index ++;
        }
        for (; index < str.length(); index ++) {
            char c = str.charAt(index);
            if (!Character.isDigit(c)) {
                break;
            }
            result = result * 10 + sign * (c - '0');
            if (result >= Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            } else if (result <= Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
        }
        return (int)result;
    }
}
```

``` python
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if not str:
            return 0

        sign, ret = 1, 0
        for i, char in enumerate(str.strip()):
            if i == 0 and char == "-":
                sign = -1
            elif i == 0 and char == "+":
                continue
            elif not char.isdigit():
                break
            else:
                ret = ret * 10 + sign * int(char)
        return min(max(ret, -2 ** 31), 2 **31 - 1)
```
