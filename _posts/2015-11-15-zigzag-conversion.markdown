---
layout: post
title: ZigZag Conversion
date: 2015-11-15 16:42:45.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</em></strong></p>


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
