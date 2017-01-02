---
layout: post
title: Decode Ways
date: 2015-11-12 12:13:00.000000000 -05:00
categories:
- Brain teaser
- Dynamic Programming
author: Jason
---
<p><strong><em>A message containing letters from A-Z is being encoded to numbers using the following mapping:<br />

'A' -> 1<br />
'B' -> 2<br />
...<br />
'Z' -> 26<br />
Given an encoded message containing digits, determine the total number of ways to decode it.</em></strong></p>
``` java
public class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0 || s.charAt(0) == '0') return 0;
        int[] count = new int[s.length() + 1];
        count[0] = 1;
        count[1] = 1;
        for (int i = 2; i <= s.length(); i++) {
            if (s.charAt(i-1) != '0') {
                count[i] = count[i-1];//0不对应任何string
            }
            int val = Integer.parseInt(s.substring(i-2, i));
            if (val >= 10 && val <= 26) {//前两位也在范围之内
                    count[i] += count[i-2];
            }
        }
        return count[s.length()];
    }
}
```
