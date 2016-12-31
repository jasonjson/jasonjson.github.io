---
layout: post
title: Contains Duplicate II
date: 2015-11-03 15:39:36.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"66ac3c645ecb8180f6ab00eb6538b33b";a:2:{s:7:"expires";i:1458053709;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:117;}i:1;a:1:{s:2:"id";i:133;}i:2;a:1:{s:2:"id";i:421;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i< nums.length; i++){
            if ((map.containsKey(nums[i]) && (i - map.get(nums[i])) <= k)) {
                return true;
            }else{
                map.put(nums[i],i);
            }
        }
        return false;
    }
}
</pre>
<p>[/expand]</p>
