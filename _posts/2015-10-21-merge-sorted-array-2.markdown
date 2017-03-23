---
layout: post
title: Merge Sorted Array
date: 2015-10-21 02:24:40.000000000 -04:00
tags:
- Algorithm
categories:
- Sorting
author: Jason
---
<p><strong><em>Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.</em></strong></p>


``` java
public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int tail1 = m - 1, tail2 = n - 1, finished = m + n - 1;
        while ( tail1 >= 0 && tail2 >= 0) {
            nums1[finished --] = nums1[tail1] > nums2[tail2] ? nums1[tail1 --] : nums2[tail2 --];
        }
        if (tail1 < 0) {
        //this can also deal with case where m = 0
            while (tail2 >= 0){
                nums1[finished --] = nums2[tail2 --];
            }
        }
    }
}
```
