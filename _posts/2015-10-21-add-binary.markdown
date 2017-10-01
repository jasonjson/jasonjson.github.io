---
layout: post
title: 67 - Add Binary
date: 2015-10-21 01:34:39.000000000 -04:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given two binary strings, return their sum (also a binary string).**

``` java
    /**
     * @param a a number
     * @param b a number
     * @return the result
     */
    public String addBinary(String a, String b) {
        // Write your code here
        int n = a.length(), m = b.length(), carry = 0;
        StringBuilder str = new StringBuilder();
        int i = n - 1, j = m - 1;
        while (carry != 0 || i >= 0 || j >= 0){
            if(i >= 0) {
                carry += Character.getNumericValue(a.charAt(i));
                i--;
            }
            if(j >= 0){
                carry += Character.getNumericValue(b.charAt(j));
                j--;
            }
            str.append(carry % 2);
            carry /= 2;
        }
        return str.reverse().toString();
    }
}
```

``` python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        ret = []
        carry, i, j = 0, len(a) - 1, len(b) - 1
        while carry or i >= 0 or j >= 0:
            if i >= 0:
                carry += int(a[i])
            if j >= 0:
                carry += int(b[j])
            ret.append(str(carry % 2))
            carry /= 2
            i -= 1
            j -= 1

        return "".join(reversed(ret))
```
