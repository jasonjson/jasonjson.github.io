---
layout: post
title: Valid Palindrome
date: 2015-10-21 02:13:45.000000000 -04:00
tags:
- Leetcode
categories:
- Palindrome
- String
author: Jason
---
<p><strong><em>Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.</em></strong></p>


``` java
public class Solution {
    /**
     * @param s A string
     * @return Whether the string is a valid palindrome
     */
    public boolean isPalindrome(String s) {
        // Write your code here
        if (s == null || s.length() == 0) return true;
        
        s = s.toLowerCase();
        int lo = 0, hi = s.length() - 1;
        while (lo <= hi) {
            while (lo <= hi && !Character.isLetterOrDigit(s.charAt(lo))) lo ++;
            while (lo <= hi && !Character.isLetterOrDigit(s.charAt(hi))) hi --;
            if (lo <= hi && s.charAt(lo) != s.charAt(hi)) {//lo <= hi必须有，不然index our of bound
                return false;
            }
            lo ++;
            hi --;
        }
        return true;
    }
}
```
