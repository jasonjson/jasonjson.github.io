---
layout: post
title: 306 - Additive Number
date: 2015-11-18 09:31:17.000000000 -05:00
tags:
- Leetcode
categories:
- DFS
author: Jason
---
**Additive number is a positive integer whose digits can form additive sequence. A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.**


``` java
import java.math.BigInteger;
public class Solution {
    public boolean isAdditiveNumber(String num) {
        if (num == null || num.length() < 3) return false;

        for (int i = 1; i <= num.length() / 2; i++) {
            if (num.charAt(0) == '0' && i > 1) break;
            BigInteger a = new BigInteger(num.substring(0, i));
            for (int j = 1; Math.max(i, j) <= num.length() - i - j; j++) {
                if (num.charAt(i) == '0' && j > 1) break;
                BigInteger b = new BigInteger(num.substring(i, i + j));
                if (isValid(num.substring(i + j), a, b)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean isValid(String num, BigInteger a, BigInteger b) {
        if (num.length() == 0) return true;

        b = a.add(b);
        a = b.subtract(a);
        String c = String.valueOf(b);
        return num.startsWith(c) && isValid(num.substring(c.length()), a, b);
    }
}
```

``` python
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return True
        for i in xrange(1, len(num) / 2 + 1):
            if num[0] == "0" and i > 1:
                break
            for j in xrange(1, len(num) - i):
                if num[i] == "0" and j > 1:
                    break
                if self.is_valid(int(num[:i]), int(num[i:i + j]), num[i + j:]):
                    return True
        return False

    def is_valid(self, prev_1, prev_2, num):
        if len(num) == 0:
            return True
        curr = str(prev_1 + prev_2)
        if num.startswith(curr) and self.is_valid(prev_2, int(curr), num[len(curr):]):
            return True
        else:
            return False
```
