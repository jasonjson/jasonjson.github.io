---
layout: post
title: Sort array
date: 2015-10-21 02:09:22.000000000 -04:00
tags: algorithm
categories:
- Sorting
author: Jason
---
<p><strong><em>Given sorted array of doubles, return the another sorted array of doubles where all elements are the squares from the input array.</em></strong></p>


``` java
public class Sort {
    public int[] getSorted(int[] arr){
        int n = arr.length;
        int[] result = new int[n];
        int lo = 0, hi = n - 1, k = n - 1;
        while (lo < hi) {
            int n1 = arr[lo] * arr[lo];
            int n2 = arr[hi] * arr[hi];
            if(n1 >= n2) {
                result[k--] = n1;
                lo++;
            } else {
                result[k--] = n2;
                hi--;
            }
        }
        return result;
    }
}
```
