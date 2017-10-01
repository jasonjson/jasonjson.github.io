---
layout: post
title: Merge Sorted Array
date: 2015-10-21 01:42:51.000000000 -04:00
tags:
- Leetcode
categories:
- Sorting
author: Jason
---
**Given two sorted integer arrays A and B, merge B into A as one sorted array.**


``` java
    /**
     * @param A: sorted integer array A which has m elements,
     *           but size of A is m+n
     * @param B: sorted integer array B which has n elements
     * @return: void
     */
    public void mergeSortedArray(int[] A, int m, int[] B, int n) {
        // write your code here
        int i = m - 1, j = n - 1, k = m + n - 1;
        while (i >= 0 && j >= 0){
        //we don't need to check if k >=0
            if (A[i] >= B[j]){
                A[k--] = A[i--];
            }else{
                A[k--] = B[j--];
            }
        }
        while(j >= 0){
            A[k--] = B[j--];
        }
        //we only need to check if B array is empty, since if B is empty, the rest of A elements would have already been in the right place.
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

        i, j, index = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
        while j >= 0:
            nums1[index] = nums2[j]
            j -= 1
            index -= 1
```
