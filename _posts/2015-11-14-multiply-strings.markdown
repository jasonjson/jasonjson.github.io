---
layout: post
title: Multiply Strings
date: 2015-11-14 21:01:30.000000000 -05:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
**Given two numbers represented as strings, return multiplication of the numbers as a string.**


``` java
public class Solution {
    public String multiply(String num1, String num2) {
        if (num1.length() == 0 || num2.length() == 0) return "";

        StringBuilder sb = new StringBuilder();
        int len1 = num1.length(), len2 = num2.length();
        int[] mul = new int[len1 + len2];
        for (int i = len1 - 1; i >= 0; i--) {
            int a = num1.charAt(i) - '0';
            int k = len2 + i;//each time we starts from the rightmost index and update each digit
            for (int j = len2 - 1; j >= 0; j--) {
                int b = num2.charAt(j) - '0';
                int c = mul[k] + a * b;
                mul[k] = c % 10;
                mul[k - 1] += c / 10;
                k --;
            }
        }
        int i = 0;
        while (i < mul.length && mul[i] == 0) i ++;
        for (; i < mul.length; i++) {
            sb.append("" + mul[i]);
        }
        return sb.length() == 0 ? "0" : sb.toString();
    }
}
```

``` python
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if not num1 or not num2:
            return ""

        ret = [0] * (len(num1) + len(num2))
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                ret[i + j] += int(n1) * int(n2)
                ret[i + j + 1] += ret[i + j] / 10
                ret[i + j] %= 10

        tmp = []
        for i, num in enumerate(reversed(ret)):
            if not (len(tmp) == 0 and num == 0):
                tmp.append(str(num))
        return "".join(tmp) if tmp else "0"
```
