---
layout: post
title: Bucket sort
date: 2015-10-26 12:49:16.000000000 -04:00
tags:
- Leetcode
categories:
- Sorting
author: Jason
---
<p><strong><em>Bucket sort an array.</em></strong></p>


``` java
public class Solution {
    public static void main(String[] args) {
        int[] A = {1,3,4,12,4,6,1,8};
        int[] B = bucketSort(A);
        for (int n : B) {
            System.out.print(n +",");
        }
    }
    public static int[] bucketSort(int[] A) {
        int max = A[0];
        for (int n : A) {
            max = Math.max(max, n);
        }
        int[] bucket = new int[max + 1];
        int[] sorted = new int[A.length];

        for (int n : A) {
            bucket[n] ++;
        }//one value in each bucket, bucket[i] stores the number of value n

        int index = 0;
        for (int i = 0; i < bucket.length; i++) {
            for (int j = 0; j < bucket[i]; j++) {//check how many duplicates
                sorted[index++] = i;
            }
        }
        return sorted;
    }
}
```
