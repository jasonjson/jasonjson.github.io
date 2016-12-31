---
layout: post
title: Binary Search
date: 2015-10-21 02:26:49.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
- Sorting
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468923752;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1087;}i:1;a:1:{s:2:"id";i:147;}i:2;a:1:{s:2:"id";i:155;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity. If the target number does not exist in the array, return -1.</em></strong><br />
[expand title="code"]</p>
<pre>
class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        //write your code here
        int lo = 0, hi = nums.length - 1, index = -1;
        while (lo <= hi){
            int mid = (lo + hi) / 2;
            if(target == nums[mid]) {
                index = mid;
                break;
            } else if (target < nums[mid]) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        while(index > 0 && nums[index-1] == target) index--;
        return index;
    }
}
</pre>
<p>[/expand]</p>
