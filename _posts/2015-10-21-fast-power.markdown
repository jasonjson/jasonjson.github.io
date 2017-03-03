---
layout: post
title: Fast Power
date: 2015-10-21 02:37:36.000000000 -04:00
tags: algorithm
categories:
- Integer
author: Jason
---
<p><strong><em>Calculate the an a^n % b where a, b and n are all 32bit integers.</em></strong></p>


``` java
class Solution {
    /*
     * @param a, b, n: 32bit integers
     * @return: An integer
     */
    public int fastPower(int a, int b, int n) {
        if (n == 1) {
            return a % b;
        } else if (n == 0) {
            return 1 % b;
        } else if (n < 0) {
            return -1;
        }
        //(a * b) % p = (a % p * b % p) % p, 将 a^n % b 分解为 (a^(n/2) * a^(n/2)) % b = ((a^(n/2) % b) * (a^(n/2) % b)) % b, deal with odd n separately.
        long result = fastPower(a, b, n/2);
        //bug1 forget to use long type
        result = result * result % b;
        if (n % 2 == 1) {
            result = result * a % b;
        }
        return (int)result;
        //bug1 forget to cast back to integer
    }
};
```
