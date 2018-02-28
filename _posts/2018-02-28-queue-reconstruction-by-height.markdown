---
layout: post
title: 406 - Queue Reconstruction By Height
date: 2018-02-28
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.**


```python
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        if not people:
            return []

        people_map = collections.defaultdict(list)
        height, ret = [], []
        for i, (h, k) in enumerate(people):
            people_map[h].append([k, i])
            if h not in height:
                height.append(h)
        height.sort(reverse=True)
        for h in height:
            people_map[h].sort()
            for (k, i) in people_map[h]:
                ret.insert(k, people[i])
        return ret
```
