---
layout: post
title: 88 - Merge Sorted Array
date: 2015-10-21 02:24:40.000000000 -04:00
tags:
- Leetcode
categories:
- Sorting
author: Jason
---
**Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.**


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

``` python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        index = m + n - 1
        while m >= 1 and n >= 1:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[index] = nums1[m - 1]
                m -= 1
            else:
                nums1[index] = nums2[n - 1]
                n -= 1
            index -= 1

        while n >= 1:
            nums1[index] = nums2[n - 1]
            n -= 1
            index -= 1
```
