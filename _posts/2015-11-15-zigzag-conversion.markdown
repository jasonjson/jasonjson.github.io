---
layout: post
title: 6 - ZigZag Conversion
date: 2015-11-15 16:42:45.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)**


``` java
public class Solution {
    public String convert(String s, int numRows) {
        if(numRows<=1) return s;
        StringBuilder sb = new StringBuilder();
        int cycle = 2 * numRows - 2; //每个cycle里有多少个数，不是多少个cycle
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < s.length(); j++) {
                if (j % cycle == i || j % cycle == (cycle - i)) {
                //除了第一个行最后一个行，其他行都有两个数满足条件
                    sb.append(s.charAt(j));
                }
            }
        }
        return sb.toString();
    }
}
```

``` python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        buckets = [[] for i in xrange(numRows)]
        i = 0
        while i < len(s):
            for j in xrange(numRows):
                if i < len(s):
                    buckets[j].append(s[i])
                    i += 1
            for j in reversed(xrange(1, numRows-1)):
                if i < len(s):
                    buckets[j].append(s[i])
                    i += 1

        ret = []
        for bucket in buckets:
            ret.extend(bucket)
        return "".join(ret)
```
