---
layout: post
title: 91 - Decode Ways
date: 2015-11-12 12:13:00.000000000 -05:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**A message containing letters from A-Z is being encoded to numbers using the following mapping:**

* A -> 1
* B -> 2
* ...
* Z -> 26

**Given an encoded message containing digits, determine the total number of ways to decode it.**


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

``` python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        #watch out edge cases
        if not s or s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1
        for i in xrange(2, len(s) + 1):
            if int(s[i - 1]) != 0:
                dp[i] += dp[i - 1]
            if int(s[i - 2 : i]) <= 26 and int(s[i - 2 : i]) >= 10:
                dp[i] += dp[i - 2]
        return dp[-1]
```
