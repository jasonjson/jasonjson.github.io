---
layout: post
title: 278 - First Bad Version
date: 2015-10-21 02:28:07.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.**


``` java
class Solution {
    /**
     * @param n: An integers.
     * @return: An integer which is the first bad version.
     */
    public int findFirstBadVersion(int n) {
        // write your code here
        if (n <= 0) return 0;
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (SVNRepo.isBadVersion(mid)) {
                hi = mid;//某个mid 不变的一定是lo < hi
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
```

``` python
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) / 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```
