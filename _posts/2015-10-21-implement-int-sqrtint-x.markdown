---
layout: post
title: Implement int sqrt(int x).
date: 2015-10-21 02:32:25.000000000 -04:00
tags: algorithm
categories:
- Brain teaser
- Integer
author: Jason
---
<p><strong><em>Compute and return the square root of x.</em></strong></p>


``` java
public class Solution {
    //newton's method
    public int mySqrt(int x) {
        long r = x;
        //bug1 : use int instead of long
        while (r * r > x) {
            r = (r + x / r) / 2;
        }
        return (int) r;
    }
    
    //binary search
    public int mySqrt(int x) {
        int lo = 1, hi = x, answer = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (mid <= x / mid) {
            //bug2 : use mid * mid <= x
            //we need to floor the result, so < is combined with = 
                lo = mid + 1;
                answer = mid;
            } else {
                hi = mid - 1;
            }
        }
        return answer;
    }
}
```
