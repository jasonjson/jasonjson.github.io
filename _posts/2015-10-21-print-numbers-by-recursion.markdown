---
layout: post
title: Print Numbers by Recursion
date: 2015-10-21 02:39:42.000000000 -04:00
tags: algorithm
categories:
- Integer
author: Jason
---
<p><strong><em>Print numbers from 1 to the largest number with N digits by recursion.</em></strong></p>


``` java
public class Solution {
    /**
     * @param n: An integer.
     * return : An array storing 1 to the largest number with n digits.
     */
    public static List<integer> numbersByRecursion(int n) {
        // write your code here
        List<integer> result = new ArrayList<integer>();
        if (n <= 0) return result;

        result.add(0);//帮忙生成10, 20, 30....
        int base = 1;
        for (int i = 1; i <= n; i++) {
            int size = result.size();
            for (int k = 1; k <= 9; k++) {
                for (int j = 0; j < size; j++) {
                    //result.add(base); 0 + base * k !!
                    result.add(result.get(j) + base * k);
                }
            }
            base *= 10;
        }
        result.remove(0);
        return result;
    }
}
```
