---
layout: post
title: 71 - Simplify Path
date: 2015-10-21 14:36:43.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an absolute path for a file (Unix-style), simplify it.**


``` java
public class Solution {
    public String simplifyPath(String path) {
        if (path == null || path.length() == 0) return "";
        String[] strs = path.split("/");
        StringBuilder sb = new StringBuilder();
        Deque<String> dq = new LinkedList<String>();
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

``` python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        if not path:
            return ""

        stack = []
        path_list = path.split("/")
        for p in path_list:
            if p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            elif p: #p can be empty string
                stack.append(p)

        return "/" + "/".join(stack)
```
