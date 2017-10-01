---
layout: post
title: Contains Duplicate III
date: 2015-11-03 16:37:27.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
- Sorting
author: Jason
---
<p><strong><em>Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.</em></strong></p>


<p><a href="https://leetcode.com/discuss/38206/ac-o-n-solution-in-java-using-buckets-with-explanation">Read more</a></p>

``` java
public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (k < 1 || t < 0) return false;
        HashMap<Long, Long> map = new HashMap<Long, Long>();
        for (int i = 0; i < nums.length; i++) {
            long newNum = (long)nums[i] - Integer.MIN_VALUE;
            long bucket = newNum / ((long)t + 1);//第几个bucket / not %
            if (map.containsKey(bucket) || (map.containsKey(bucket - 1) && Math.abs(map.get(bucket - 1) - newNum) <= t) || (map.containsKey(bucket + 1) && Math.abs(map.get(bucket + 1) - newNum) <= t)) {
                return true;
            }
            if (map.size() == k) {
                Long last = ((long)(nums[i - k]) - Integer.MIN_VALUE) / ((long)t + 1);
                map.remove(last);
            }
            map.put(bucket, newNum);
        }
        return false;
    }
}
```
