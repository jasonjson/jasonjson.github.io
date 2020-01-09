---
layout: post
title: 45 - Jump Game II
date: 2020-01-09 21:02:23.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps.**


``` java
public class Solution {
    //The main idea is based on greedy. Let's say the range of the current jump is [curBegin, curEnd], curFarthest is the farthest point that all points in [curBegin, curEnd] can reach. Once the current point exceeds curEnd, then trigger another jump, and set the new curEnd with curFarthest, then keep the above steps, as the following:
    public int jump(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        int rightmost = 0, end = 0, count = 0;
        for (int i = 0; i < nums.length - 1; i++) {//!!nums.length - 1, when we are at the last index, we are finished. We don't need to consider the value at last index
            rightmost = Math.max(rightmost, nums[i] + i);
            if (i == end) {
                count ++;
                end = rightmost;
                if (end >= nums.length - 1) {
                    break;
                }
            }
        }
        return count;
    }
}
```

``` python
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0

        rightmost = count = end = 0
        for i in range(len(nums) - 1):
            rightmost = max(rightmost, i + nums[i])
            if i == end:
                count += 1
                end = rightmost
                if end >= len(nums) - 1:
                    break
        return count
```

``` python
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if i - j <= nums[j]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
```
