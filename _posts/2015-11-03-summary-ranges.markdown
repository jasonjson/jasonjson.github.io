---
layout: post
title: Summary Ranges
date: 2015-11-03 12:00:26.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given a sorted integer array without duplicates, return the summary of its ranges.<br />

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].</em></strong></p>
``` java
public class Solution {
    public List<string> summaryRanges(int[] nums) {
        List<string> result = new ArrayList<>();
        if (nums == null || nums.length == 0) return result;
        
        int i = 0;
        while (i < nums.length) {
            int j = i + 1;
            while (j < nums.length && nums[j] == nums[j - 1] + 1) {
                j ++;
            }
            if (j - i == 1) {
                String range = String.valueOf(nums[i]);
                result.add(range);
            } else {
                String range = nums[i] + "->" + nums[j - 1];
                result.add(range);
            }
            i = j;
        }
        return result;
    }
}
```
