---
layout: post
title: 163 - Missing Ranges
date: 2015-11-05 15:07:38.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges. For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].**


``` java
public class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> result = new ArrayList<String>();
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

``` python
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            return [self.helper(lower, upper)]

        ret = []
        if lower < nums[0]:
            ret.append(self.helper(lower, nums[0] - 1))
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] + 1:
                ret.append(self.helper(nums[i - 1] + 1, nums[i] - 1))
        if upper > nums[-1]:
            ret.append(self.helper(nums[-1] + 1, upper))
        return ret

    def helper(self, lo, hi):
        return str(lo) if lo == hi else str(lo) + "->" + str(hi)
```
