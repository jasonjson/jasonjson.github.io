---
layout: post
title: Majority Element II
date: 2015-10-21 02:40:45.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Integer
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1461066928;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:2071;}i:1;a:1:{s:2:"id";i:421;}i:2;a:1:{s:2:"id";i:542;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an integer array of size n, find all elements that appear more than $\floor *{n/3}$ times. The algorithm should run in linear time and in O(1) space.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public List<integer> majorityElement(int[] nums) {
        if (nums == null) return null;
        List<integer> result = new ArrayList<integer>();
        int key1 = -1, key2 = -1, count1 = 0, count2 = 0;
        for (int n : nums) {
            if (count1 == 0) {
                key1 = n;
                count1 = 1;
            } else if (count2 == 0 && n != key1) {
                key2 = n;
                count2 = 1;
            } else {
                if (key1 == n) {
                    count1 ++;
                } else if (key2 == n) {
                    count2 ++;
                } else {
                    count1 --;
                    count2 --;
                }
            }
        }
        count1 = 0;
        count2 = 0;
        for (int n : nums) {
            if (key1 == n) {
                count1++;
            } else if (key2 == n) {
                count2++;
            }
        }
        if(count1 > nums.length / 3) result.add(key1);
        if(count2 > nums.length / 3) result.add(key2);
        return result;
    }
}
</integer></integer></integer></pre>
<p>[/expand]</p>
