---
layout: post
title: Palindrome Permutation
date: 2015-10-30 15:34:35.000000000 -04:00
tags: algorithm
categories:
- Palindrome
- Permutation
author: Jason
---
<p><strong><em>Given a string, determine if a permutation of the string could form a palindrome.</em></strong></p>


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
