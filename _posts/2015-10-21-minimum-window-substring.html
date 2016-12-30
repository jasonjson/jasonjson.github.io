---
layout: post
title: Minimum Window Substring
date: 2015-10-21 13:05:04.000000000 -04:00
type: post
published: true
status: publish
categories:
- String
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469246671;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:393;}i:1;a:1:{s:2:"id";i:396;}i:2;a:1:{s:2:"id";i:503;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a string source and a string target, find the minimum window in source which will contain all the characters in target.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param source: A string
     * @param target: A string
     * @return: A string denote the minimum window
     *          Return "" if there is no such a string
     */
    public String minWindow(String source, String target) {
        if (source == null || source.length() == 0 || target == null || target.length() == 0) return "";
        
        int m = source.length(), n = target.length();
        int start = 0, begin = 0, found = 0, min_win = Integer.MAX_VALUE;
        int[] source_cnt = new int[256], target_cnt = new int[256];
        for (char c : target.toCharArray()) {
            target_cnt[c] ++;
        }
        for (int i = 0; i < m; i++) {
            char c = source.charAt(i);
            source_cnt[c]++;
            if (target_cnt[c] >= source_cnt[c]) {
                found ++;// not source_cnt[c] >= target_cnt[c]
            }
            if (found == n) {
                while (source_cnt[source.charAt(start)] > target_cnt[source.charAt(start)]) {
                    source_cnt[source.charAt(start++)] --;
                }
                if (min_win > i - start + 1) {
                    min_win = i - start + 1;
                    begin = start;
                }
            }
        }
        return min_win == Integer.MAX_VALUE ? "" : source.substring(begin, begin + min_win);
    }
}
</pre>
<p>[/expand]</p>
