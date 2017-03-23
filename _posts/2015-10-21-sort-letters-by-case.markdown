---
layout: post
title: Sort Letters by Case
date: 2015-10-21 14:38:36.000000000 -04:00
tags:
- Algorithm
categories:
- Sorting
author: Jason
---
<p><strong><em>Given a string which contains only letters. Sort it by lower case first and upper case second.</em></strong></p>


``` java
public class Solution {
    /** 
     *@param chars: The letter array you should sort by Case
     *@return: void
     */
    public void sortLetters(char[] chars) {
        //write your code here
        if (chars == null || chars.length == 0) return;
        
        int lo = 0, hi = chars.length - 1;
        while (lo <= hi) {
            while (lo <= hi && chars[lo] > 'Z') lo ++;
            while (lo <= hi && chars[hi] < 'a') hi --;
            if (lo <= hi) {
                swap(chars, lo, hi);
            }
        }
    }
    
    public void swap(char[] chars, int a, int b) {
        char temp = chars[a];
        chars[a] = chars[b];
        chars[b] = temp;
    }
}
```
