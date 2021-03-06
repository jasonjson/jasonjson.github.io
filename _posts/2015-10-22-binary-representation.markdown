---
layout: post
title: Binary Representation
date: 2015-10-22 08:28:06.000000000 -04:00
tags:
- Leetcode
categories:
- Integer
author: Jason
---
<p><strong><em>Given a (decimal - e.g. 3.72) number that is passed in as a string, return the binary representation that is passed in as a string. If the fractional part of the number can not be represented accurately in binary with at most 32 characters, return ERROR.</em></strong></p>


``` java
public class Solution {
    public String binaryRepresentation(String n) {
        if (n == null || n.length() == 0) return "";
        
        StringBuilder left_binary = new StringBuilder(), right_binary = new StringBuilder();
        int i = 0;
        for (; i < n.length(); i++) {
            if (n.charAt(i) == '.') {
                break;
            }
        }
        int left = Integer.parseInt(n.substring(0, i));
        double right = Double.parseDouble(n.substring(i));
        while (left > 0) {
            left_binary.append(left % 2);
            left /= 2;
        }
        while (right > 0) {
            right *= 2;
            if (right >= 1) {
                right_binary.append(1);
                right -= 1;
            } else {
                right_binary.append(0);
            }
        }//key: corner cases
        if (right_binary.length() >= 32) {
            return "ERROR";
        } else if (right_binary.length() == 0 && left_binary.length() == 0) {
            return "0"; //input 0.0
        } else if (right_binary.length() == 0) {//input 1.0 output 1 not 1.0
            return left_binary.reverse().toString();
        } else if (left_binary.length() == 0) {//input 0.5 output 0.1 not .1
            return "0." + right_binary;
        } else {
            return left_binary.reverse().toString() + "." + right_binary;
        }
    }
}
```
