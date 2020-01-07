---
layout: post
title: 621 - Task Scheduler
date: 2020-01-06
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle. However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle. You need to return the least number of intervals the CPU will take to finish all the given tasks.**

```python
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0

        task_num = list(Counter(tasks).values())
        most_frequent = max(task_num)
        most_frequent_counts = task_num.count(most_frequent)
        return max(len(tasks), (n + 1) * (most_frequent - 1) + most_frequent_counts)
```
