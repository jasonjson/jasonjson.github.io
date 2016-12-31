---
layout: post
title: Generate Parentheses
date: 2015-11-15 11:41:02.000000000 -05:00
type: post
published: true
status: publish
categories:
- DFS Backtracking
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464715246;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1267;}i:1;a:1:{s:2:"id";i:1302;}i:2;a:1:{s:2:"id";i:536;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<string> generateParenthesis(int n) {
        List<string> result = new ArrayList<string>();
        helper(n, n, "", result);
        return result;
    }
    
    public void helper(int left, int right, String path, List<string> result) {
        if (left == 0 && right == 0) {
            result.add(path);
            return;
        }
        if (left > right || left < 0 || right < 0) {
            //when the number of "(" left to add is larger than the number of ")", stop
            return;
        }
        helper(left - 1, right, path + "(", result);
        helper(left, right - 1, path + ")", result);
    }
}
</string></string></string></string></pre>
<p>[/expand]</p>
