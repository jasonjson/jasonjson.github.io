---
layout: post
title: Course Schedule
date: 2015-11-04 12:41:18.000000000 -05:00
tags:
- Leetcode
categories:
- Graph
- Sorting
author: Jason
---
<p><strong><em>There are a total of n courses you have to take, labeled from 0 to n - 1. Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]. Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?</em></strong></p>

``` java
public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (prerequisites == null || prerequisites.length == 0) return true;

        int[] degree = new int[numCourses];
        List<List<integer>> course = new ArrayList<List<integer>>();
        for (int i = 0; i < numCourses; i++) {
            course.add(new ArrayList<integer>());
        }
        for (int[] pair : prerequisites) {
            degree[pair[0]] ++;
            course.get(pair[1]).add(pair[0]);
        }
        Queue<integer> q = new LinkedList<integer>();
        for (int i = 0; i < numCourses; i++) {
            if (degree[i] == 0) {
                q.offer(i);
            }
        }
        while (!q.isEmpty()) {
            int curr = q.poll();
            numCourses --;
            for (int next : course.get(curr)) {
                degree[next]--;
                if (degree[next] == 0) {
                    q.offer(next);
                }
            }
        }
        return numCourses == 0;
    }
}
```

```python
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True

        degrees = {}
        graphs = {}
        #Build graph
        for i in xrange(numCourses):
            degrees.setdefault(i, 0)
        for requirement in prerequisites:
            degrees[requirement[0]] += 1
            prerequisite = graphs.setdefault(requirement[1], [])
            prerequisite.append(requirement[0])

        #Traverse graph
        queue = deque()
        for key, val in degrees.items():
            if val == 0:
                queue.append(key)

        while queue:
            curr = queue.popleft()
            numCourses -= 1
            for next in graphs.get(curr, []):
                degrees[next] -= 1
                if (degrees[next] == 0):
                    queue.append(next)

        return numCourses == 0
```
