---
layout: post
title: Count of Smaller Numbers After Self
date: 2015-12-07 18:21:09.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
- Sorting
author: Jason
---
<p><strong><em>You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].</em></strong></p>


``` java
public class Solution {
    public List<integer> countSmaller(int[] nums) {
        List<integer> result = new ArrayList<integer>();
        if (nums == null || nums.length == 0) return result;

        List<integer> sorted = new ArrayList<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            int index = find(sorted, nums[i]);
            result.add(index);
            sorted.add(index,nums[i]);
        }
        Collections.reverse(result);//!!don't forget to reverse
        return result;
    }

    public int find(List<integer> sorted, int val) {
        //if (sorted.size() == 0) return 0; no need
        int lo = 0, hi = sorted.size() - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (sorted.get(mid) == val) {
                while (mid - 1 >= 0 && sorted.get(mid - 1) == val) {
                    mid--;
                }
                return mid;
            } else if (sorted.get(mid) < val) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
}
```
