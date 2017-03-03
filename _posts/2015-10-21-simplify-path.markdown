---
layout: post
title: Simplify Path
date: 2015-10-21 14:36:43.000000000 -04:00
tags: algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given an absolute path for a file (Unix-style), simplify it.</em></strong></p>


``` java
public class Solution {
    public String simplifyPath(String path) {
        if (path == null || path.length() == 0) return "";
        String[] strs = path.split("/");
        StringBuilder sb = new StringBuilder();
        Deque<string> dq = new LinkedList<string>();
        for (String s : strs) {
            if (s.length() == 0 || s.equals(".")) {
                continue;
            } else if (s.equals("..")) {
                if (!dq.isEmpty()) {//一定要先检查dp是否为空
                    dq.removeLast();
                }
            } else {
                dq.addLast(s);
            }
        }
        if (dq.isEmpty()) {
            return "/";
        } else {
            while (!dq.isEmpty()) {
                sb.append("/" + dq.removeFirst());
            }
            return sb.toString();
        }
    }
}
```
