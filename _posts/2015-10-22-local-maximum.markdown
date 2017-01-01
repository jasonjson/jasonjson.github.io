---
layout: post
title: Local maximum
date: 2015-10-22 14:50:21.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466093957;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:423;}i:1;a:1:{s:2:"id";i:145;}i:2;a:1:{s:2:"id";i:1038;}}}}
  _inbound_impressions_count: '0'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Suppose we are given an array A[1···n] with the special property that A[1] ≤ A[2] and A[n − 1] >= A[n]. We say that an element A[i] is a local maximum if it is less than or equal to both its neighbors, or more formally, if A[i − 1] ≤ A[i] and A[i] ≥ A[i + 1]. For example, there are four local maximum in the following array: We can obviously find a<br />
local maximum in O(n) time by scanning through the array. Describe and analyze an algorithm that finds one local maximum in O(log n) time. (It is enough if your algorithm finds one local maximum. There is no need to find all local maxima.)</em></strong></p>
<p>[expand title="code"]</p>
<pre>
class Solution {
    public static int localMax(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        int lo = 1, hi = nums.length - 2;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] > nums[mid + 1] && nums[mid] > nums[mid - 1]) {
                return nums[mid];
            } else if (nums[mid] < nums[mid + 1]) {
                //two cases : nums[mid] > nums[mid - 1] or nums[mid] < nums[mid - 1]
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return -1;
    }
}
</pre>
<p>[/expand]</p>
