---
layout: post
title: Remove Element
date: 2015-10-21 02:16:55.000000000 -04:00
type: post
published: true
status: publish
categories:
- Integer
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1455574035;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1038;}i:1;a:1:{s:2:"id";i:1578;}i:2;a:1:{s:2:"id";i:384;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array and a value, remove all instances of that value in place and return the new length. The order of elements can be changed. It doesn't matter what you leave beyond the new length.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        for(int n : nums){
            if(n != val){
                //if n != val, we increment i
                nums[i++] = n;
            }
            //if n==val, we don't increment i, and nums[i] will be overwritten by n
        }
        return i;
    }
}
</pre>
<p>[/expand]</p>
