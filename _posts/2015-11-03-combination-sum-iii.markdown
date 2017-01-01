---
layout: post
title: Combination Sum III
date: 2015-11-03 17:04:46.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464364807;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:536;}i:1;a:1:{s:2:"id";i:1240;}i:2;a:1:{s:2:"id";i:335;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<List<integer>> combinationSum3(int k, int n) {
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (k <= 0 || n <= 0) return result;
        helper(1, k, n, new ArrayList<integer>(), result);
        return result;
    }
    public void helper(int start, int k, int remain, List<integer> path, List<List<integer>> result) {
        if (k == 0) {
            if (remain == 0) {
                result.add(new ArrayList<integer>(path));
            }
            return;
        }
        for (int i = start; i <= 9; i++) {
            if (i > remain) {
                return;
            }
            path.add(i);
            helper(i + 1, k - 1, remain - i, path, result);
            path.remove(path.size() - 1);
        }
    }
}
</integer></integer></integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
