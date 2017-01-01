---
layout: post
title: Pascal's Triangle
date: 2015-11-09 17:17:27.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467705370;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1450;}i:1;a:1:{s:2:"id";i:1671;}i:2;a:1:{s:2:"id";i:347;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given numRows, generate the first numRows of Pascal's triangle.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public List<List<integer>> generate(int numRows) {
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (numRows <= 0) return result;
        for (int i = 1; i <= numRows; i++) {
            List<integer> list = new ArrayList<integer>();
            for (int j = 0; j < i; j++) {
                if (j == 0) {
                    list.add(1);
                } else if (j == i - 1) {
                    list.add(1);
                } else {
                    list.add(result.get(result.size() - 1).get(j - 1) + result.get(result.size() - 1).get(j));
                }
            }
            result.add(list);
        }
        return result;
    }
}
</integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
