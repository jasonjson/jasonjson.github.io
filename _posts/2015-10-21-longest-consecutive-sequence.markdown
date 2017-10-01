---
layout: post
title: Longest Consecutive Sequence
date: 2015-10-21 14:26:41.000000000 -04:00
tags:
- Leetcode
categories:
- Integer
- Subarray
author: Jason
---
<p><strong><em>Given an unsorted array of integers, find the length of the longest consecutive elements sequence.</em></strong></p>


``` java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return an integer
     */
    public int longestConsecutive(int[] num) {
        // write you code here
        if (num == null || num.length == 0) return 0;
        int len = 0;
        Set<Integer> set = new HashSet<Integer>();
        for (int n : num) {
            set.add(n);
        }
        
        for (int n : num) {
            int left = n;
            while (set.remove(left)) {
                left--;
            }
            int right = n + 1;
            while (set.remove(right)) {
                right ++;
            }
            len = Math.max(len, right - left - 1);
        }
        return len;
    }
}
```
