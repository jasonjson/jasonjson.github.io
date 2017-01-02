---
layout: post
title: Shortest Palindrome
date: 2015-11-03 17:45:22.000000000 -05:00
categories:
- Brain teaser
- Two Pointers
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
                 i = 0; //重新开始,必须从第一个字母开始找
                 end--; //关键是找到end,是包括首字母的最长的palindrome
                 j = end;
             }
        }
        return new StringBuilder(s.substring(end+1)).reverse().toString() + s;
    }
}
```
