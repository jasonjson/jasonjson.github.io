---
layout: post
title: Validate UTF-8 byte sequence,
date: 2016-01-21 12:09:57.000000000 -05:00
categories:
- Data Structure
author: Jason
---
<p><strong><em><a href="https://en.wikipedia.org/wiki/UTF-8#Description">Reference</a></em></strong></p>


``` java
public class Solution {
    public static boolean validate(byte[] bytes) {
        int expectedLen;
        if (bytes.length == 0) {
            return false;
        } else if ((bytes[0] & 0b10000000) == 0b00000000) {
            expectedLen = 1;
        } else if ((bytes[0] & 0b11100000) == 0b11000000) {
            expectedLen = 2;
        } else if ((bytes[0] & 0b11110000) == 0b11100000) {
            expectedLen = 3;
        } else if ((bytes[0] & 0b11111000) == 0b11110000) {
            expectedLen = 4;
        } else if ((bytes[0] & 0b11111100) == 0b11111000) {
            expectedLen = 5;
        } else if ((bytes[0] & 0b11111110) == 0b11111100) {
            expectedLen = 6;
        } else {
            return false;
        }
        if (expectedLen != bytes.length) {
            return false;
        }
        for (int i = 1; i < bytes.length; i++) {
            if ((bytes[i] & 0b11000000) != 0b10000000) {
                return false;
            }
        }
        return true;
    }
}
```
