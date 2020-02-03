---
layout: post
title: 727 - Minimum Window Subsequence
date: 2020-02-03
tags:
- Leetcode
categories:
- String
author: Jason
---
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W. If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

```python
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        dp = [[-1] * (len(S) + 1) for _ in range(len(T) + 1)]
        #dp[i][j] starting index for T[i - 1] -> S[j - 1]
        for j in range(len(S) + 1):
            dp[0][j] = j

        for i in range(1, len(T) + 1):
            for j in range(1, len(S) + 1):
                if T[i - 1] == S[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        min_len = len(S) + 1
        start = 0
        for j, index in enumerate(dp[-1]):
            if index != -1 and j - index < min_len: #j - 1 - index + 1
                start = index
                min_len = j - index
        return S[start: start + min_len] if min_len <= len(S) else ""
```
