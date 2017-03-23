---
layout: post
title: Delete Digits
date: 2015-10-21 14:02:50.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
- Integer
author: Jason
---
<p><strong><em>Given string A representative a positive integer which has N digits, remove any k digits of the number, the remaining digits are arranged according to the original order to become a new positive integer. Find the smallest integer after remove k digits.</em></strong></p>


``` java
public class Solution {
    /**
     *@param A: A positive integer which has N digits, A is a string.
     *@param k: Remove k digits.
     *@return: A string
     */
    public String DeleteDigits(String A, int k) {
        // write your code here
        if (A == null || A.length() == 0 || k <= 0) return A;
        
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < A.length(); j++) {
                if (j == A.length() - 1 || A.charAt(j) > A.charAt(j + 1)) {//bug: forget j == A.length() -1 
                    A = A.substring(0, i) + A.substring(i+1);
                    //start from left, when we find a number larger than its right number, remove it, thus it will be replaced by a smaller number
                    break;//bug: forget break
                }
            }
        }
        int i = 0;
        while (i < A.length() && A.charAt(i) == '0') {
            i ++; //remove zeroes in the front
        }
        return A.substring(i);
    }
}
```
