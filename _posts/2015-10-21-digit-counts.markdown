---
layout: post
title: Digit Counts
date: 2015-10-21 14:03:43.000000000 -04:00
categories:
- Brain teaser
- Integer
author: Jason
---
<p><strong><em>Count the number of k's between 0 and n. k can be 0 - 9.</em></strong></p>

``` java
class Solution {
    /*
     * param k : As description.
     * param n : As description.
     * return: An integer denote the count of digit k in 1..n
     */
    public int digitCounts(int k, int n) {
        if (k == 0 && n == 0) return 1;
        int result = 0, base = 1;
        while (n / base != 0) {
            if (k == 0 && base > 1) break; //k == 0, then 01 or 001 or 0001 are not numbers
            int hi = n / (base * 10);
            int curr = n / base % 10;
            int lo = n % base;
            if (curr > k) {
                result += (hi + 1) * base;
            } else if (curr == k) {
                result += hi * base + lo + 1;
            } else {
                result += hi * base;
            }
            base *= 10;
        }
        return result;
    }
};
```
