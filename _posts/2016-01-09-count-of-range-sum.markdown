---
layout: post
title: Count of Range Sum
date: 2016-01-09 23:37:50.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive. Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.</em></strong></p>


``` java
public class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        if (nums == null || nums.length == 0) return 0;
        
        long[] sum = new long[nums.length + 1];
        for (int i = 1; i <= nums.length; i++) {
            sum[i] = sum[i - 1] + nums[i - 1];
        }
        return helper(sum, 0, sum.length, lower, upper);
    }
    public int helper(long[] sum, int start, int end, int lower, int upper) {
        if (start + 1 >= end) return 0;
        int mid = (start + end) / 2;
        int result = helper(sum, start, mid, lower, upper) + helper(sum, mid, end, lower, upper);
        int k = mid, l = mid, r = mid;
        long[] cache = new long[end - start];
        for (int i = start, j = 0; i < mid; ++i, ++j) {
            while (k < end && sum[k] - sum[i] < lower) k++;
            while (l < end && sum[l] - sum[i] <= upper) l++;
            while (r < end && sum[r] < sum[i]) cache[j++] = sum[r++];
            cache[j] = sum[i];
            result += l - k;
        }
        System.arraycopy(cache, 0, sum, start, r - start);
        return result;
    }
}
```
``` java
public class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        if (nums == null || nums.length == 0) return 0;
        
        int[] sum = new int[nums.length + 1];
        for (int i = 1; i <= nums.length; i++) {
            sum[i] = sum[i - 1] + nums[i - 1];
        }
        int count = 0;
        for (int i = 0; i + 1 <= nums.length; i++) {
            for (int j = i + 1; j <= nums.length; j++) {
                if (sum[j] - sum[i] >= lower && sum[j] - sum[i] <= upper) {
                    count ++;
                }
            }
        }
        return count;
    }
}
```
``` java
public class Solution {
    public static void main(String[] args) {
        int[] nums = {-2, 5, -1};
        System.out.println(countRangeSum(nums, -2, 2));
    }
    public static int countRangeSum(int[] nums, int lower, int upper) {
        if (nums == null || nums.length == 0) return 0;

        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i; j < nums.length; j++) {
                int sum = 0;
                for (int k = i; k <= j; k++) {
                    sum += nums[k];
                }
                if (sum >= lower && sum <= upper) {
                    count ++;
                }
            }

        }
        return count;
    }
}
```
