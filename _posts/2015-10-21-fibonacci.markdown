---
layout: post
title: Fibonacci
date: 2015-10-21 02:38:49.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>Find the Nth number in Fibonacci sequence. A Fibonacci sequence is defined as follow: The first two numbers are 0 and 1. The ith number is the sum of i-1th number and i-2 th number.</em></strong></p>


``` java
class Solution {
    /**
     * @param n: an integer
     * @return an integer f(n)
     */
    
    public static HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
    //create a static hashmap to be used during recursion
    public int fibonacci(int n) {
        if (n <= 0) return -1;
        if (n == 1) return 0;
        if (n == 2) return 1;
        if (map.containsKey(n)) {
            return map.get(n);
        }
        int result = fibonacci(n-1) + fibonacci(n-2);
        map.put(n, result);
        return result;
    }
}
```
