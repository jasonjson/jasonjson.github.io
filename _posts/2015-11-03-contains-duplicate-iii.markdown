---
layout: post
title: Contains Duplicate III
date: 2015-11-03 16:37:27.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Sorting
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466777970;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1298;}i:1;a:1:{s:2:"id";i:1038;}i:2;a:1:{s:2:"id";i:1974;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.</em></strong></p>
<p><a href="https://leetcode.com/discuss/38206/ac-o-n-solution-in-java-using-buckets-with-explanation">Read more</a><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (k < 1 || t < 0) return false;
        HashMap<Long, Long> map = new HashMap<Long, Long>();
        for (int i = 0; i < nums.length; i++) {
            long newNum = (long)nums[i] - Integer.MIN_VALUE;
            long bucket = newNum / ((long)t + 1);//第几个bucket / not %
            if (map.containsKey(bucket) || (map.containsKey(bucket - 1) && Math.abs(map.get(bucket - 1) - newNum) <= t) || (map.containsKey(bucket + 1) && Math.abs(map.get(bucket + 1) - newNum) <= t)) {
                return true;
            }
            if (map.size() == k) {
                Long last = ((long)(nums[i - k]) - Integer.MIN_VALUE) / ((long)t + 1);
                map.remove(last);
            }
            map.put(bucket, newNum);
        }
        return false;
    }
}
</pre>
<p>[/expand]</p>
