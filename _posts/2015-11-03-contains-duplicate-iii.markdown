---
layout: post
title: 220 - Contains Duplicate III
date: 2015-11-03 16:37:27.000000000 -05:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.**
[Reference](https://leetcode.com/discuss/38206/ac-o-n-solution-in-java-using-buckets-with-explanation")


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

``` python
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0:
            return False
        bucket_map = {}
        bucket_size = t + 1
        for i in xrange(len(nums)):
            index = nums[i] / bucket_size
            if index in bucket_map:
                return True
            if index - 1 in bucket_map and abs(nums[i] - bucket_map[index - 1]) < bucket_size:
                return True
            if index + 1 in bucket_map and abs(nums[i] - bucket_map[index + 1]) < bucket_size:
                return True
            bucket_map[index] = nums[i]
            if i >= k:
                del bucket_map[nums[i - k] / bucket_size]
        return False
```
