---
layout: post
title: Minimum Window Substring
date: 2015-10-21 13:05:04.000000000 -04:00
categories:
- String
author: Jason
---
<p><strong><em>Given a string source and a string target, find the minimum window in source which will contain all the characters in target.</em></strong></p>


``` java
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
```
