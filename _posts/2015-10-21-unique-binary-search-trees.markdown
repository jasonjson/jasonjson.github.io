---
layout: post
title: Unique Binary Search Trees
date: 2015-10-21 02:36:32.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given n, how many structurally unique BST's (binary search trees) that store values 1...n?**

```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1]
        for i in range(2, n + 1):
            amount = 0
            for j in range(0, i):
                amount += dp[j] * dp[i - j - 1]
            dp.append(amount)
        return dp[n]
```

``` java
public class Solution {
    /**
     * @paramn n: An integer
     * @return: An integer
     */
    public int numTrees(int n) {
        // write your code here
        if (n < 0) return -1;
        int[] count = new int[n+1]; //count[i] indicates how many BST for i
        count[0] = 1;
        for (int i = 1; i <= n; i++) {//there can be i - 1 elements in the subtree, use j to control how many elements in left subtree and how many in right subtree, update count[i]
            for (int j = 0; j < i; j++) {
                count[i] += count[j] * count[i - j - 1];// j  + (i - j - 1) == i - 1 elements
            }
        }
        return count[n];
    }
}
```

``` python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n + 1)
        dp[0] = 1
        for i in xrange(1, n + 1):
            for j in xrange(i):
                #j elements in left tree and i - j - 1 elements in right tree
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]
```
