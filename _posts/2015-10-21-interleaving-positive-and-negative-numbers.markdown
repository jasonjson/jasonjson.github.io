---
layout: post
title: Interleaving Positive and Negative Numbers
date: 2015-10-21 14:21:54.000000000 -04:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.</em></strong></p>


``` java
class Solution {
    public void rerange(int[] A) {
        if (A == null || A.length == 0) return;
        int negCnt = 0, posCnt = 0;
        for (int n : A) {
            if (n > 0) {
                posCnt ++;
            } else {
                negCnt ++;
            }
        }//put negative or positive number first
        int pos = 0, neg = 1;
        if (posCnt < negCnt) {
            pos = 1;
            neg = 0;
        }
        //quick sort
        while (pos < A.length && neg < A.length) {
            while (pos < A.length && A[pos] > 0) {
                pos += 2;
            }
            while (neg < A.length && A[neg] < 0) {
                neg += 2;
            }
            if (pos < A.length && neg < A.length) {
                swap(A, pos, neg);
            }
        }
   }
   
   public void swap(int[] nums, int a, int b) {
       int temp = nums[a];
       nums[a] = nums[b];
       nums[b] = temp;
   }
}
```
