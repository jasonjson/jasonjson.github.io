---
layout: post
title: 139 - Subarray Sum Closest
date: 2015-10-21 02:18:36.000000000 -04:00
tags:
- Lintcode
categories:
- Array
author: Jason
---
**Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.**


``` java
public class Solution {
    class pair {
        int sum, index;
        public pair(int sum, int index) {
            this.sum = sum;
            this.index = index;
        }
    }
    public int[] subarraySumClosest(int[] nums) {
        if (nums == null || nums.length == 0) return new int[] {};

        pair[] pairs = new pair[nums.length + 1];
        pairs[0] = new pair(0, 0);
        for (int i = 1; i <= nums.length; i++) {
            pairs[i] = new pair(pairs[i-1].sum + nums[i - 1], i);
        }
        Arrays.sort(pairs, new Comparator<pair>() {
           public int compare(pair a, pair b) {
               return a.sum - b.sum;
           }
        });
        int diff = Integer.MAX_VALUE, start = 0, end = 0;
        for (int i = 1; i < pairs.length; i++) {
            //after sorting, the min distance must be within neighbors
            if (diff > pairs[i].sum - pairs[i - 1].sum) {
                diff = pairs[i].sum - pairs[i - 1].sum;
                start = Math.min(pairs[i].index, pairs[i-1].index);
                end = Math.max(pairs[i].index, pairs[i-1].index) - 1;
            }
        }
        return new int[] {start, end};
    }
}
```

``` python
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        if not nums:
            return []

        sum_list = [[0, 0]]
        for i, num in enumerate(nums):
            curr_sum = sum_list[-1][0] + num
            sum_list.append([curr_sum, i + 1])
        sum_list.sort(key=lambda x : x[0])
        min_sum = 2 ** 31 - 1
        start = end = 0
        for i in xrange(1, len(sum_list)):
            diff = sum_list[i][0] - sum_list[i - 1][0]
            if min_sum > diff:
                start = min(sum_list[i - 1][1], sum_list[i][1])
                end = max(sum_list[i - 1][1], sum_list[i][1]) - 1
                min_sum = diff
        return [start, end]
```
