---
layout: post
title: 214 - Shortest Palindrome
date: 2015-11-03 17:45:22.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.</em></strong></p>


``` java
public class Solution {
//The key point is to find the longest palindrome starting from the first character, and then reverse the remaining part as the prefix to s.
    public String shortestPalindrome(String s) {
        int i = 0, end = s.length() - 1, j = end;
        while (i < j) {
             if (s.charAt(i) == s.charAt(j)) {
                 i++;
                 j--;
             } else {
                 i = 0;
                 end--;
                 j = end;
             }
        }
        return new StringBuilder(s.substring(end+1)).reverse().toString() + s;
    }
}
```

``` python
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        i = 0
        j = end = len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                i = 0
                end -= 1
                j = end
        return "".join(reversed(s[end + 1:])) + s
```
