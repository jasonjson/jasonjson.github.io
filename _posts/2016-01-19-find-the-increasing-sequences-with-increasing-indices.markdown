---
layout: post
title: Find the increasing sequences with increasing indices
date: 2016-01-19 17:00:31.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Find three numbers in an array such that a &lt; b &lt; c and indices of a b c are also in ascending order</em></strong></p>

``` java
public class Solution {
    public static void main(String[] args) {
        int[] nums = {8, 7, 6, 12, 14};
        get(nums);
    }
    public static int[] get(int[] nums) {
        if (nums == null || nums.length == 0) return new int[]{};

        int n = nums.length;
        int[] result = new int[3], min = new int[n], max = new int[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                min[i] = nums[i];
            } else {
                min[i] = Math.min(min[i - 1], nums[i - 1]);
            }
        }
        for (int i = n - 1; i >= 0; i--) {
            if (i == n - 1) {
                max[i] = nums[i];
            } else {
                max[i] = Math.max(max[i + 1], nums[i + 1]);
            }
        }//find the max number after i and min number before i
        for (int i = 0; i < n; i++) {
            if (nums[i] > min[i] && nums[i] < max[i]) {
                result[0] = min[i];
                result[1] = nums[i];
                result[2] = max[i];
                break;
            }
        }
        return result;
    }
}
```
