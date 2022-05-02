---
layout: post
title: 12 - Integer to Roman
date: 2015-10-21 14:20:00.000000000 -04:00
tags:
- Leetcode
categories:
- Integer
author: Jason
---
**Given an integer, convert it to a roman numeral. The number is guaranteed to be within the range from 1 to 3999.**


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

``` python
class Solution:
    def intToRoman(self, num: int) -> str:
        if not num:
            return ""
        roman = ["M", "D", "C", "L", "X", "V", "I"]
        scale = 1000
        ret = []
        for i in range(0, 7, 2):
            digit = num // scale
            if digit <= 3:
                for j in range(digit):
                    ret.append(roman[i])
            elif digit == 4:
                ret.extend([roman[i], roman[i - 1]])
            elif digit == 5:
                ret.append(roman[i - 1])
            elif digit <= 8:
                ret.append(roman[i - 1])
                for j in range(digit - 5):
                    ret.append(roman[i])
            elif digit == 9:
                ret.extend([roman[i], roman[i - 2]])
            num %= scale
            scale //= 10

        return "".join(ret)
```
