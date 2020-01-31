---
layout: post
title: 207 - Course Schedule
date: 2015-11-04 12:41:18.000000000 -05:00
tags:
- Leetcode
categories:
- Graph
author: Jason
---
**There are a total of n courses you have to take, labeled from 0 to n - 1. Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]. Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?**

``` python
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        weight_map = {i: 0 for i in range(numCourses)}
        course_map = defaultdict(list)
        for a, b in prerequisites:
            course_map[b].append(a)
            weight_map[a] += 1

        queue = [c for c in weight_map if weight_map[c] == 0]
        while queue:
            curr = queue.pop(0)
            numCourses -= 1
            for node in course_map[curr]:
                weight_map[node] -= 1
                if weight_map[node] == 0:
                    queue.append(node)

        return numCourses == 0
```
