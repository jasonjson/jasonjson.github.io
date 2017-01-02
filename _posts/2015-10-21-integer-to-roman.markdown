---
layout: post
title: Integer to Roman
date: 2015-10-21 14:20:00.000000000 -04:00
categories:
- Integer
author: Jason
---
<p><strong><em>Given an integer, convert it to a roman numeral. The number is guaranteed to be within the range from 1 to 3999.</em></strong></p>

``` java
public class Solution {
    public String intToRoman(int n) {
        StringBuilder result = new StringBuilder();
        int scale = 1000;
        String[] roman = {"I","V","X","L","C","D","M"};
        for (int i = 6; i >= 0; i -= 2) {
            int digit = n / scale;
            if (digit <= 3) {
                for (int j = 0; j < digit; j++) {
                    result.append(roman[i]);
                }
            } else if (digit == 4) {
                result.append(roman[i]).append(roman[i+1]);
            } else if (digit == 5) {
                result.append(roman[i+1]);
            } else if (digit <= 8) {
                result.append(roman[i+1]);
                for (int j = 0; j < digit - 5; j++) {
                    result.append(roman[i]);
                }
            } else if (digit == 9) {
                result.append(roman[i]).append(roman[i+2]);
            }
            n %= scale;
            scale /= 10;
        }
        return result.toString();
    }
}
```
