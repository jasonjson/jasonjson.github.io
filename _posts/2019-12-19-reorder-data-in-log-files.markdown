---
layout: post
title: 937-reorder-data-in-log-files - Py
date: 2019-12-19
tags:
- Leetcode
categories:
- Array
author: Jason
---
**You have an array of logs.  Each log is a space delimited string of words. For each log, the first word in each log is an alphanumeric identifier.  Then, either:**

* Each word after the identifier will consist only of lowercase letters, or;
* Each word after the identifier will consist only of digits.

**We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier. Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order. Return the final order of the logs.**

```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def sort_key(log):
            ident, rest = log.split(" ", 1)
            return (0, rest, ident) if rest[0].isalpha() else (1, )
        logs.sort(key=sort_key)
        return logs
```
