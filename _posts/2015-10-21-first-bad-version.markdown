---
layout: post
title: First Bad Version
date: 2015-10-21 02:28:07.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464328400;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1087;}i:1;a:1:{s:2:"id";i:153;}i:2;a:1:{s:2:"id";i:991;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.</em></strong><br />
[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
