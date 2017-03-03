---
layout: post
title: Partition Array by Odd and Even
date: 2015-10-21 02:25:58.000000000 -04:00
tags: algorithm
categories:
- Integer
- Sorting
author: Jason
---
<p><strong><em>Partition an integers array into odd number first and even number second.</em></strong></p>


``` java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: nothing
     */
    public void partitionArray(int[] nums) {
        // write your code here;
        int start = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 != 0) {
                int temp = nums[start];
                nums[start++] = nums[i];
                nums[i] = temp;
            }
        }
    }
}
```

``` java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: nothing
     */
    public void partitionArray(int[] nums) {
        // similar to quick sort;
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi){
            while (lo <= hi && nums[lo] % 2 != 0) {lo++;}
            while (lo <= hi && nums[hi] % 2 == 0) {hi--;}
            if(lo < hi){
                int temp = nums[lo];
                nums[lo] = nums[hi];
                nums[hi] = temp;
                lo++;
                hi--;
            }
        }
    }
}
```
