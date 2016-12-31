---
layout: post
title: Factor Combinations
date: 2015-11-02 07:28:09.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1458989812;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1302;}i:1;a:1:{s:2:"id";i:536;}i:2;a:1:{s:2:"id";i:1267;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Numbers can be regarded as product of its factors. For example,<br />
8 = 2 x 2 x 2;<br />
  = 2 x 4.<br />
Write a function that takes an integer n and return all possible combinations of its factors.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public static List<List<integer>> getFactors(int n) {
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (n <= 1) return result;

        helper(n, 2, new ArrayList<integer>(), result);
        return result;
    }

    public static void helper(int remain, int start, List<integer> path, List<List<integer>> result) {
        if (remain == 1) {
            if (path.size() > 1) {//for 12, {12} can be in the result, we need to remove it
                result.add(new ArrayList<integer>(path));
            }
            return;
        }
        for (int i = start; i <= remain; i++) {
            if (remain % i == 0) {
                path.add(i);
                helper(remain / i, i, path, result);{//first problem, i can be equal to n, for 37 we use path.size() > 1 to get the empty result, second problem, we use start to avoid duplicate results, like for 10, the result can be [2, 5] and [5, 2]
                path.remove(path.size() - 1);
            }
        }
    }
}
</integer></integer></integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
