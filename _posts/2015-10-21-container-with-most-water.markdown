---
layout: post
title: Container With Most Water
date: 2015-10-21 13:26:44.000000000 -04:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1461790462;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:587;}i:1;a:1:{s:2:"id";i:589;}i:2;a:1:{s:2:"id";i:936;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param heights: an array of integers
     * @return: an integer
     */
    public int maxArea(int[] heights) {
        if (heights == null || heights.length == 0) return 0;
        
        int result = 0, left = 0, right = heights.length - 1;
        while (left < right) {
            result = Math.max(result, (right - left) * Math.min(heights[left], heights[right]));
            if (heights[left] < heights[right]) {
                left ++;
            } else {
                right --;
            }
        }
        return result;
    }//https://leetcode.com/discuss/1074/anyone-who-has-a-o-n-algorithm
    //http://www.cnblogs.com/tenosdoit/p/3812880.html
}
</pre>
<p>[/expand]</p>
