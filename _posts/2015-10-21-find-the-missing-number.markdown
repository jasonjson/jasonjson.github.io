---
layout: post
title: Find the Missing Number
date: 2015-10-21 13:02:42.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given an array contains N numbers of 0 .. N, find which number doesn't exist in the array.</em></strong></p>


``` java
public class Solution {
    public int missingNumber(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int count = 0;
            for (int n : nums) {
                if (n <= mid) {
                    count ++;
                }
            }
            if (count == mid + 1) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
}
```
``` java
public class Solution {
    /**    
     * @param nums: an array of integers
     * @return: an integer
     */
    public int findMissing(int[] nums) {
        // write your code here
        int x1 = 0;
        for (int n : nums) {
            x1 ^= n;
        }        
        int x2 = 0;
        for (int i = 0; i <= nums.length; i++) {
            x2 ^= i;
        }
        return x1 ^ x2;
    }
    public int findMissing(int[] nums) {
        // write your code here
        bucketSort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                return i;
            }
        }
        return nums.length;
    }
    //bucket sort
    public void bucketSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] != i) {
                if (nums[i] == nums.length) {
                    break;
                } //nums[nums.length] out of bounds
                int nextNum = nums[nums[i]];
                nums[nums[i]] = nums[i];
                nums[i] = nextNum;
            }
        }
    }
}
```
