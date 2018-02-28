---
layout: post
title: 388 - Longest Absolute File Path
date: 2017-11-11
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.**


```python
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        if not input:
            return 0
        path_list = input.split("\n")
        len_list = [0] * len(path_list)
        max_len = 0
        for path in path_list:
            level = path.count("\t")
            #\t does not count as path
            len_list[level] = len(path) - level
            if "." in path:
                max_len = max(max_len, sum(len_list[:level + 1]) + level)
        return max_len
```
