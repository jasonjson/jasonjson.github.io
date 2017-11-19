---
layout: post
title: 128 - Longest Consecutive Sequence
date: 2015-10-21 14:26:41.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an unsorted array of integers, find the length of the longest consecutive elements sequence.**


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

``` python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_set = set(nums)
        ret = 0
        for num in nums:
            left, right = num, num + 1
            while left in nums_set:
                nums_set.discard(left) #o(1)
                left -= 1
            while right in nums_set:
                nums_set.discard(right)
                right += 1
            ret = max(ret, right - left - 1)
        return ret
```
