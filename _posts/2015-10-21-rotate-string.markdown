---
layout: post
title: Rotate String
date: 2015-10-21 02:12:52.000000000 -04:00
tags:
- Algorithm
categories:
- String
author: Jason
---
<p><strong><em>Given a string and an offset, rotate string by offset. (rotate from left to right)</em></strong></p>


``` java
public class Solution {
    /**
     * @param str: an array of char
     * @param offset: an integer
     * @return: nothing
     */
    public void rotateString(char[] str, int offset) {
        // write your code here
        int n = str.length;
        if(str == null || n == 0) return; //error check!!
        offset %= n; //in case offset is bigger than n
        reverse(str, 0, n-offset-1);
        //take an example and experiment the index carefully
        reverse(str, n-offset, n-1);
        reverse(str, 0, n-1);
    }
    
    public void reverse(char[] str, int lo, int hi){
        while(lo < hi){
            char temp = str[hi];
            str[hi] = str[lo];
            str[lo] = temp;
            lo++;
            hi--;
        }
    }
}
```
