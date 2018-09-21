---
layout: post
title: 198 - House Robber
date: 2015-10-21 14:15:26.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.**


``` java
    /**
     * @param A: An array of non-negative integers.
     * return: The maximum amount of money you can rob tonight
     */
    public long houseRobber(int[] A) {
        // write your code here
        if (A == null || A.length == 0) return 0;
        long sum1 = 0, sum2 = 0;
        for (int i = 0; i < A.length; i++) {
            if (i % 2 == 0) {
                sum1 += A[i];
                sum1 = Math.max(sum1, sum2);
            } else {
                sum2 += A[i];
                sum2 = Math.max(sum1, sum2);
            }
        }
        return Math.max(sum1, sum2);
    }
    //DP
    public long houseRobber(int[] A) {
        if (A.length <= 0) return 0;
        if (A.length == 1) return A[0];

        long[] dp = new long[A.length];
        dp[0] = A[0];
        dp[1] = Math.max(A[0], A[1]);
        for (int i = 2; i < A.length; i++) {
            dp[i] = Math.max(A[i] + dp[i-2], dp[i-1]);
        }
        return dp[A.length - 1];
    }
}
```

``` python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            max_p = max(dp[-1], dp[-2] + nums[i])
            dp.append(max_p)
        return dp[-1]
```
