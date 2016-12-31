---
layout: post
title: Edit Distance
date: 2015-10-21 12:45:39.000000000 -04:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467182826;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1501;}i:1;a:1:{s:2:"id";i:410;}i:2;a:1:{s:2:"id";i:77;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.) You have the following 3 operations permitted on a word: Insert a character, Delete a character, Replace a character</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int minDistance(String word1, String word2) {
        int len1 = word1.length(), len2 = word2.length();
        int[][] dist = new int[len1 + 1][len2 + 1];
        for (int i = 0; i <= len1; i ++) {
            dist[i][0] = i;
        }
        for (int j = 0; j <= len2; j ++) {
            dist[0][j] = j;
        }
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (word1.charAt(i-1) == word2.charAt(j-1)) {
                    dist[i][j] = dist[i-1][j-1];
                } else {
                    dist[i][j] = Math.min(dist[i-1][j-1], Math.min(dist[i-1][j], dist[i][j-1])) + 1;
                }
            }
        }
        return dist[len1][len2];
    }
}
</pre>
<p>[/expand]</p>
