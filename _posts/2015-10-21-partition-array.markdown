---
layout: post
title: Partition Array
date: 2015-10-21 02:20:04.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
- Subarray
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465994082;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:443;}i:1;a:1:{s:2:"id";i:1124;}i:2;a:1:{s:2:"id";i:421;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that: All elements &lt; k are moved to the leff. All elements >= k are moved to the right Return the partitioning index, i.e the first index i nums[i] >= k.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /** 
     *@param nums: The integer array you should partition
     *@param k: As description
     *return: The index after partition
     */
    public int partitionArray(int[] nums, int k) {
        //write your code here
        int i = 0, j = nums.length - 1;
        while (i <= j) {
            while (i <= j && nums[i] < k) i++;
            while (i <= j && nums[j] >= k) j--;
            if (i < j) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j--;
            }
        }
        return i;
    }
}
</pre>
<p>[/expand]</p>
