---
layout: post
title: Strobogrammatic Number II
date: 2015-11-02 11:43:03.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466933995;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1258;}i:1;a:1:{s:2:"id";i:1302;}i:2;a:1:{s:2:"id";i:1267;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). Find all strobogrammatic numbers that are of length = n.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<string> findStrobogrammatic(int n) {
        return helper(n, n);
    }
    
    public List<string> helper(int n, int m) {
        if (n == 0) return new ArrayList<string>(Arrays.asList(""));
        if (n == 1) return new ArrayList<string>(Arrays.asList("0", "1", "8"));
        List<string> prev = helper(n - 2, m); //like count and say
        List<string> result = new ArrayList<string>();
        for (int i = 0; i < prev.size(); i++) {
            String s = prev.get(i);
            if (n != m) {
                result.add("0" + s + "0");//0 can't be the first number
            }
            result.add("1" + s + "1");
            result.add("8" + s + "8");
            result.add("6" + s + "9");
            result.add("9" + s + "6");
        }
        return result;
    }
}
</string></string></string></string></string></string></string></pre>
<p>[/expand]</p>
