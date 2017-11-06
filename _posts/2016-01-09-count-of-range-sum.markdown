---
layout: post
title: 327 - Count of Range Sum
date: 2016-01-09 23:37:50.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive. Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.**


``` java
public class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        if (nums == null || nums.length == 0) return 0;

        long[] sum = new long[nums.length + 1];
        for (int i = 1; i <= nums.length; i++) {
            sum[i] = sum[i - 1] + nums[i - 1];
        }
        return helper(sum, 0, sum.length, lower, upper);
    }
    public int helper(long[] sum, int start, int end, int lower, int upper) {
        if (start + 1 >= end) return 0;
        int mid = (start + end) / 2;
        int result = helper(sum, start, mid, lower, upper) + helper(sum, mid, end, lower, upper);
        int k = mid, l = mid, r = mid;
        long[] cache = new long[end - start];
        for (int i = start, j = 0; i < mid; ++i, ++j) {
            while (k < end && sum[k] - sum[i] < lower) k++;
            while (l < end && sum[l] - sum[i] <= upper) l++;
            while (r < end && sum[r] < sum[i]) cache[j++] = sum[r++];
            cache[j] = sum[i];
            result += l - k;
        }
        System.arraycopy(cache, 0, sum, start, r - start);
        return result;
    }
}
```

``` python
class SegmentNode(object):
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
        self.count = 0
        self.left = None
        self.right = None

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        set_nums = set()
        sums = 0
        for num in nums:
            sums += num
            set_nums.add(sums)
        list_nums = list(set_nums)
        list_nums.sort()
        root = self.build_tree(list_nums, 0, len(list_nums) - 1)

        ret = 0
        for num in reversed(nums):
            self.update_tree(root, sums)
            sums -= num
            ret += self.get_count(root, lower + sums, upper + sums)
        return ret;

    def build_tree(self, nums, lo, hi):
        if lo > hi:
            return
        root = SegmentNode(nums[lo], nums[hi])
        if lo != hi:
            mid = (lo + hi) / 2
            root.left = self.build_tree(nums, lo, mid)
            root.right = self.build_tree(nums, mid + 1, hi)
        return root

    def update_tree(self, node, val):
        if not node:
            return
        elif node.lo <= val and node.hi >= val:
            node.count += 1
            self.update_tree(node.left, val)
            self.update_tree(node.right, val)

    def get_count(self, node, lo, hi):
        if not node or lo > node.hi or hi < node.lo:
            return 0
        elif lo <= node.lo and hi >= node.hi:
            return node.count
        else:
            return self.get_count(node.left, lo, hi) + self.get_count(node.right, lo, hi)
```
