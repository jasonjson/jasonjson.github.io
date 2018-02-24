---
layout: post
title: 246 - Strobogrammatic Number
date: 2015-11-02 11:10:54.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). Write a function to determine if a number is strobogrammatic. The number is represented as a string. For example, the numbers "69", "88", and "818" are all strobogrammatic.**


``` java
public class Solution {
    public boolean isStrobogrammatic(String num) {
        if (num.length() == 0) return true;
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        map.put('1', '1');
        map.put('8', '8');
        map.put('0', '0');
        map.put('6', '9');
        map.put('9', '6');
        int lo = 0, hi = num.length() - 1;
        while (lo <= hi) {
            char c = num.charAt(lo);
            if (!map.containsKey(c) || map.get(num.charAt(lo)) != num.charAt(hi)) {
                return false;
            }
            lo ++;
            hi --;
        }
        return true;
    }
}
```

``` python
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """

        mapping = {"1" : "1", "0": "0", "6":"9", "8": "8", "9":"6"}
        lo, hi = 0, len(num) - 1
        while lo <= hi:
            if mapping.get(num[lo], None) != num[hi]:
                return False
            lo += 1
            hi -= 1
        return True
```
