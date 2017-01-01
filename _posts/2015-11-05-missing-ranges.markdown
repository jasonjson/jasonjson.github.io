---
layout: post
title: Missing Ranges
date: 2015-11-05 15:07:38.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465429424;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1258;}i:1;a:1:{s:2:"id";i:2006;}i:2;a:1:{s:2:"id";i:1284;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.<br />
For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<string> findMissingRanges(int[] nums, int lower, int upper) {
        List<string> result = new ArrayList<string>();
        if (nums.length == 0) {
            result.add(range(lower, upper));
            return result;
        }
        if (lower < nums[i]) {
            result.add(range(lower, nums[i] - 1));
        }
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] - nums[i - 1] > 1) {
               result.add(range(nums[i - 1] + 1, nums[i] - 1));
            }
        }
        if (upper > nums[nums.length - 1] {
            result.add(range(nums[nums.length - 1] + 1, upper));
        }
        return result;
    }
    
    public String range(int n, int m) {
        return n == m ? String.valueOf(n) : n + "->" + m;
    }
}
</string></string></string></pre>
<p>[/expand]</p>
