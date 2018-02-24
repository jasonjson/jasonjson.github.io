---
layout: post
title: 228 - Summary Ranges
date: 2015-11-03 12:00:26.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a sorted integer array without duplicates, return the summary of its ranges. For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].**


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
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if not nums:
            return []

        ret = []
        start = 0
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i - 1] + 1:
                ret.append(self.helper(nums[start], nums[i - 1]))
                start = i
        ret.append(self.helper(nums[start], nums[-1]))
        return ret

    def helper(self, num1, num2):
        if num1 == num2:
            return str(num1)
        else:
            return str(num1) + "->" + str(num2)
```
