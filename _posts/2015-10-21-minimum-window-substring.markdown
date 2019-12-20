---
layout: post
title: 76 - Minimum Window Substring
date: 2015-10-21 13:05:04.000000000 -04:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a string source and a string target, find the minimum window in source which will contain all the characters in target.**


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

``` python
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        start = found = 0
        ret = ""
        counter_t = Counter(t)
        counter_s = Counter()
        for i, c in enumerate(s):
            counter_s[c] += 1
            if counter_s[c] == counter_t[c]:
                found += 1
            while found == len(counter_t):
                if not ret or i - start + 1 < len(ret):
                    ret = s[start:i+1]
                counter_s[s[start]] -= 1
                if counter_s[s[start]] < counter_t[s[start]]:
                    found -= 1
                start += 1
        return ret
```
