---
layout: post
title: Missing Ranges
date: 2015-11-05 15:07:38.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.</p>

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].</em></strong></p>
``` java
public class Solution {
    public List<string> findMissingRanges(int[] nums, int lower, int upper) {
        List<string> result = new ArrayList<string>();
        if (nums.length == 0) {
            result.add(range(lower, upper));
            return result;
        }
        if (lower < nums[i]) {
            result.add(range(lower, nums[i] - 1));
        }
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] - nums[i - 1] > 1) {
               result.add(range(nums[i - 1] + 1, nums[i] - 1));
            }
        }
        if (upper > nums[nums.length - 1] {
            result.add(range(nums[nums.length - 1] + 1, upper));
        }
        return result;
    }
    
    public String range(int n, int m) {
        return n == m ? String.valueOf(n) : n + "->" + m;
    }
}
```
