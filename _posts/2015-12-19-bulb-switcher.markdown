---
layout: post
title: Bulb Switcher
date: 2015-12-19 10:23:55.000000000 -05:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.</em></strong></p>


``` java
//1. locker #k is opened toggled for each factor of k. For instance, locker 15 is opened on rounds 1, 3, 5, 15.
//2. If the number of rounds if odd, then the locker will remain open. If the number of rounds is even, the the lock will remain closed.
//3. Only perfect square numbers have odd number of factors. For instance, 16 has 1, 2, 4, 8, 16. 32 has 1, 2, 4, 8, 16, 32. 36 has 1, 2, 3, 4, 6, 9, 12, 18, 36.
public class Solution {
    public int bulbSwitch(int n) {
        if (n <= 0) return 0;
        return (int)Math.sqrt(n);
    }
}
```

``` java
public class Solution {
    public int bulbSwitch(int n) {
        if (n <= 0) return 0;
        
        boolean[] bulb = new boolean[n + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (j % i == 0) {
                    bulb[j] = !bulb[j];
                }
            }
        }
        int count = 0;
        for (int i = 1; i < bulb.length; i++) {
            if (bulb[i]) {
                count ++;
            }
        }
        return count;
    }
}
```
