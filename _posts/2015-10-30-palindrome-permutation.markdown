---
layout: post
title: 266 - Palindrome Permutation
date: 2015-10-30 15:34:35.000000000 -04:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a string, determine if a permutation of the string could form a palindrome.**


``` java
public class Solution {
    public boolean canPermutePalindrome(String s) {
       if (s == null || s.length() == 0) return false;

       int[] count = new int[256];
       for (char c : s.toCharArray()) {
           if (count[c] > 0) {
               count[c] --;
           } else {
               count[c] ++;
           }
       }
       int single = 0;
       for (int n : count) {
           if (n != 0) {
               single ++;
           }
           if (single > 1) {
               return false;
           }
       }
       return true;
    }
}
```

``` python
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        char_count = collections.Counter(s)
        found_single = False
        for count in char_count.values():
            if count % 2 != 0:
                if found_single:
                    return False
                found_single = True
        return True
```
