---
layout: post
title: Add Digits
date: 2015-10-31 10:40:28.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
- Integer
author: Jason
---
<p><strong><em>Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.</p>

For example:</p>
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.</p>
Follow up:</p>
Could you do it without any loop/recursion in O(1) runtime?</em></strong></p>

``` java
public class Solution {
    public int addDigits(int num) {
        if (num == 0) return 0;
        return num % 9 == 0 ? 9 : num % 9;//观察结果 与9相关
    }
}
```

``` java
public class Solution {
    public int addDigits(int num) {
        String s = String.valueOf(num);
        while (s.length() > 1) {
            int sum = 0;
            for (char c : s.toCharArray()) {
                sum += Character.getNumericValue(c);
            }
            s = String.valueOf(sum);
        }
        return Integer.parseInt(s);
    }
}
```
``` java
public class Solution {
    public int addDigits(int num) {
        int temp = 0;
        while (num > 0) {
            temp += num % 10;
            if (temp >= 10) {
                temp = temp % 10 + temp / 10;
            } 
            num /= 10;
        }
        return temp;
    }
}
```
