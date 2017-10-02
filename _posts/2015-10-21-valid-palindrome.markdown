---
layout: post
title: 125 - Valid Palindrome
date: 2015-10-21 02:13:45.000000000 -04:00
tags:
- Leetcode
categories:
- Palindrome
- String
author: Jason
---
**Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.**


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
            if !(Character.isLetterOrDigit(s.charAt(lo))) {
                lo ++;
                continue;
            }
            if (!Character.isLetterOrDigit(s.charAt(hi))) {
                hi --;
                continue;
            }
            if (s.charAt(lo) != s.charAt(hi)) {//lo <= hi必须有，不然index our of bound
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
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        lo, hi = 0, len(s) - 1
        while lo <= hi:
            if not s[lo].isalnum():
                lo += 1
                continue
            if not s[hi].isalnum():
                hi -= 1
                continue
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1
        return True
```
