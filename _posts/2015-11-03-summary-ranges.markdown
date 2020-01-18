---
layout: post
title: 228 - Summary Ranges
date: 2020-01-18
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
Given a sorted integer array without duplicates, return the summary of its ranges. For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].


``` java
public class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();
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

``` python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ret = [[nums[0]]]
        for num in nums[1:]:
            prev = ret[-1][-1]
            if num > prev + 1:
                ret.append([num])
            else:
                ret[-1][1:] = num,
        return ["->".join(map(str, n)) for n in ret]
```
