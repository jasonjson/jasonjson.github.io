---
layout: post
title: Patching Array
date: 2016-01-27 14:15:01.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.</em></strong></p>


``` java
//Let miss be the smallest sum in [1,n] that we might be missing. Meaning we already know we can build all sums in [1,miss). Then if we have a number num <= miss in the given array, we can add it to those smaller sums to build all sums in [1,miss+num). If we don't, then we must add such a number to the array, and it's best to add miss itself, to maximize the reach.
public class Solution {
    public int minPatches(int[] nums, int n) {
        long miss = 1;
        int result = 0, i = 0;
        while (miss <= n) {
            if (i < nums.length && nums[i] <= miss) {
                miss += nums[i++];
            } else {
                miss += miss;
                result ++;
            }
        }
        return result;
    }
}
```
``` java
public class Solution {
    public int minPatches(int[] nums, int n) {
        if (nums == null || nums.length == 0) return 0;

        HashMap<Integer, Integer> map = new HashMap<>();
        helper(nums, 0, 0, map);
        List<integer> missing = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (!map.containsKey(i)) {
                missing.add(i);
            }
        }
        int result = 0;
        for (int miss : missing) {
            if (!map.containsKey(miss)) {
                result++;
                List<integer> elements = new ArrayList<>();
                elements.addAll(map.keySet());
                for (int key : elements) {
                    map.put(key + miss, 1);
                }
            }
        }
        return result;
    }

    public void helper(int[] nums, int start, int sum, HashMap<Integer, Integer>map) {
        if (sum != 0) {
            map.put(sum, 1);
        }
        for (int i = start; i < nums.length; i++) {
            helper(nums, i + 1, sum + nums[i], map);
        }
    }
}
```
