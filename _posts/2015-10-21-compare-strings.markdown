---
layout: post
title: Compare Strings
date: 2015-10-21 02:11:25.000000000 -04:00
tags:
- Algorithm
categories:
- String
author: Jason
---
<p><strong><em>Compare two strings A and B, determine whether A contains all of the characters in B. The characters in string A and B are all Upper Case letters.</em></strong></p>


``` java
public class Solution {
    /**
     * @param A : A string includes Upper Case letters
     * @param B : A string includes Upper Case letter
     * @return :  if string A contains all of the characters in B return true else return false
     */
    public boolean compareStrings(String A, String B) {
        // write your code here
        if (B.length() == 0) return true;//error check !!!
        if (A.length() == 0) return false;
        
        int[] letters = new int[26];
        for (char c : A.toCharArray()) {
            letters[c - 'A'] ++;
        }
        for (char c : B.toCharArray()) {
            if (--letters[c - 'A'] < 0) {
                return false;
            }
        }
        return true;
    }   
```
