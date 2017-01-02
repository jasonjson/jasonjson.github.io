---
layout: post
title: First Bad Version
date: 2015-10-21 02:28:07.000000000 -04:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.</em></strong><br />


``` java
/**
 * public class VersionControl {
 *     public static boolean isBadVersion(int k);
 * }
 * you can use VersionControl.isBadVersion(k) to judge whether 
 * the kth code version is bad or not.
*/
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
