---
layout: post
title: Shortest Word Distance
date: 2015-11-02 13:35:25.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469245637;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1265;}i:1;a:1:{s:2:"id";i:1263;}i:2;a:1:{s:2:"id";i:121;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list. You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        int index1 = -1, index2 = -1, min = Integer.MAX_VALUE;
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1)) {
                index1 = i;
            } else if (words[i].equals(word2)) {
                index2 = i;
            }
            if (index1 != -1 && index2 != -1) {
                min = Math.min(min, Math.abs(index1 - index2));
            }
        }
        return min;
    }
}
</pre>
<p>[/expand]</p>
