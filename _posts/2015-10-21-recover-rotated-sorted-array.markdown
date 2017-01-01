---
layout: post
title: Recover Rotated Sorted Array
date: 2015-10-21 02:19:02.000000000 -04:00
type: post
published: true
status: publish
categories:
- Sorting
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1456381967;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1758;}i:1;a:1:{s:2:"id";i:936;}i:2;a:1:{s:2:"id";i:157;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a rotated sorted array, recover it to sorted array in-place.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param nums: The rotated sorted array
     * @return: void
     */
    public void recoverRotatedSortedArray(ArrayList<integer> nums) {
        // write your code
        int len = nums.size();
        int index = 0;
        while(index < len-1 && nums.get(index) <= nums.get(index+1)){
        //the element can be the same, so <= is important
            index++;
        }
        reverseUtil(nums,0,index);
        reverseUtil(nums,index+1,len-1);
        reverseUtil(nums,0,len-1);
    }
    //reverse an arraylist
    public void reverseUtil(ArrayList<integer> nums, int lo, int hi){
        if(lo > hi) return;
        for(int i = lo; i <= hi; i++){
            nums.add(i,nums.remove(hi));
        }
    }
}
</integer></integer></pre>
<p>[/expand]</p>
