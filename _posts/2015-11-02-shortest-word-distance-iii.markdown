---
layout: post
title: Shortest Word Distance III
date: 2015-11-02 13:37:36.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"6dfaf861da919bdcc556f641bdc2ca9d";a:2:{s:7:"expires";i:1467115606;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1263;}i:1;a:1:{s:2:"id";i:121;}i:2;a:1:{s:2:"id";i:149;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.<br />
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.<br />
word1 and word2 may be the same and they represent two individual words in the list.<br />
You may assume word1 and word2 are both in the list.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        int index1 = -1, index2 = -1, min = Integer.MAX_VALUE;
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1)) {
                index1 = i;
            }
            if (index1 != -1 && index2 != -1 && index1 != index2) {
                min = Math.min(min, Math.abs(index1 - index2));
            }//case["a","a"], word1 = "a", word2 ＝ "a" 更新index2前 算一次
            if (words[i].equals(word2)) {
                index2 = i;
            }
            if (index1 != -1 && index2 != -1 && index1 != index2) {
                min = Math.min(min, Math.abs(index1 - index2));
            }//更新后算一个
        }
        return min;
    }
}
</pre>
<p>[/expand]</p>
