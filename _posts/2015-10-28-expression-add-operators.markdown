---
layout: post
title: Expression Add Operators
date: 2015-10-28 12:58:06.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- DFS Backtracking
tags:
- Leetcode
meta:
  _wpcom_is_markdown: '1'
  _wpas_done_all: '1'
  _edit_last: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466826269;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:339;}i:1;a:1:{s:2:"id";i:1267;}i:2;a:1:{s:2:"id";i:1424;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.</em></strong></p>
<p><a href="http://segmentfault.com/a/1190000003797204">Read more</a><br />
[expand title = "code"]</p>
<pre>
public class Solution {
    public List<string> addOperators(String num, int target) {
        List<string> result = new ArrayList<string>();
        if (num == null || num.length() == 0) return result;
        
        helper(num, target, 0, 0, "", result);
        return result;
    }
    
    public void helper(String num, int target, long prev, long currRes, String path, List<string> result) {
        if (num.length() == 0 && currRes == target) {
            result.add(new String(path));
            return;
        }
        for (int i = 1; i <= num.length(); i++) {
            String newStr = num.substring(0, i);
            if (newStr.charAt(0) == '0' && i > 1) return;//illegal numbers 01, 0123
            long newNum = Long.parseLong(newStr);//use long
            if (path.length() == 0) {//check if it's the first number
                helper(num.substring(i), target, newNum, newNum, path + newStr, result);
            } else {
                helper(num.substring(i), target, newNum, currRes + newNum, path + "+" + newStr, result);
                helper(num.substring(i), target, -newNum, currRes - newNum, path + "-" + newStr, result);
                helper(num.substring(i), target, prev * newNum, currRes - prev + prev * newNum, path + "*" + newStr, result);
            }
        }
    }
}
</string></string></string></string></pre>
<p>[/expand]</p>
