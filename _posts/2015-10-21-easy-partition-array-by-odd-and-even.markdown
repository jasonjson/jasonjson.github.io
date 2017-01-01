---
layout: post
title: Partition Array by Odd and Even
date: 2015-10-21 02:25:58.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
- Sorting
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466265070;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:139;}i:1;a:1:{s:2:"id";i:559;}i:2;a:1:{s:2:"id";i:1073;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Partition an integers array into odd number first and even number second.</em></strong><br />
[expand title= "code1"]</p>
<pre>
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: nothing
     */
    public void partitionArray(int[] nums) {
        // write your code here;
        int start = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 != 0) {
                int temp = nums[start];
                nums[start++] = nums[i];
                nums[i] = temp;
            }
        }
    }
}
</pre>
<p>[/expand]<br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: nothing
     */
    public void partitionArray(int[] nums) {
        // similar to quick sort;
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi){
            while (lo <= hi && nums[lo] % 2 != 0) {lo++;}
            while (lo <= hi && nums[hi] % 2 == 0) {hi--;}
            if(lo < hi){
                int temp = nums[lo];
                nums[lo] = nums[hi];
                nums[hi] = temp;
                lo++;
                hi--;
            }
        }
    }
}
</pre>
<p>[/expand]</p>
