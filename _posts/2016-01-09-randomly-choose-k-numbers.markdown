---
layout: post
title: Randomly Choose k Samples
date: 2016-01-09 10:29:27.000000000 -05:00
tags:
- OA
categories:
- Brain Teaser
author: Jason
---
**Reservoir sampling is a family of randomized algorithms for randomly choosing k samples from a list of n items, where n is either a very large or unknown number.**

[Reference](http://www.geeksforgeeks.org/reservoir-sampling)

``` java
public class Solution {
    public static int[] randamPick(int[] arr, int k) {
        int[] result = new int[k];
        int i = 0;
        for (; i < k; i++) {
            result[i] = arr[i];
        }
        Random rand = new Random();
        for (; i < arr.length; i++) {
            int j = rand.nextInt(i + 1);
            if (j < k) {
                result[j] = arr[i];
            }
        }
        return result;
    }
}
```
