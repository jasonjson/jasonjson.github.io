---
layout: post
title: Strobogrammatic Number
date: 2015-11-02 11:10:54.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465083227;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1208;}i:1;a:1:{s:2:"id";i:1562;}i:2;a:1:{s:2:"id";i:1668;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).<br />
Write a function to determine if a number is strobogrammatic. The number is represented as a string.<br />
For example, the numbers "69", "88", and "818" are all strobogrammatic.</em></strong></p>
<p>[expand title = "hashmap"]</p>
<pre>
public class Solution {
    public boolean isStrobogrammatic(String num) {
        if (num.length() == 0) return true;
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        map.put('1', '1');
        map.put('8', '8');
        map.put('0', '0');
        map.put('6', '9');
        map.put('9', '6');
        int lo = 0, hi = num.length() - 1;
        while (lo <= hi) {
            char c = num.charAt(lo);
            if (!map.containsKey(c) || map.get(num.charAt(lo)) != num.charAt(hi)) {
                return false;
            }
            lo ++;
            hi --;
        }
        return true;
    }
}
</pre>
<p>[/expand]<br />
[expand title="recursive"]</p>
<pre>
public class Solution {
    public boolean isStrobogrammatic(String num) {
        if (num.length() == 0) return true;
        if (num.length() == 1) {
            return num.equals("1") || num.equals("8") || num.equals("0");
        }
        char c1 = num.charAt(0), c2 = num.charAt(num.length() - 1);
        if ((c1 == '6' && c2 == '9') || (c1 == '9' && c2 == '6') || (c1 == '8' && c2 == '8') || (c1 == '1' && c2 == '1') || (c1 == '0' && c2 == '0')) {
            return isStrobogrammatic(num.substring(1, num.length() - 1));
        } else {
            return false;
        }
    }
}
</pre>
<p>[/expand]</p>
