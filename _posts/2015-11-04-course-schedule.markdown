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

``` java
public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (prerequisites == null || prerequisites.length == 0) return true;

        int[] degree = new int[numCourses];
        List<List<Integer>> course = new ArrayList<List<Integer>>();
        for (int i = 0; i < numCourses; i++) {
            course.add(new ArrayList<Integer>());
        }
        for (int[] pair : prerequisites) {
            degree[pair[0]] ++;
            course.get(pair[1]).add(pair[0]);
        }
        Queue<Integer> q = new LinkedList<Integer>();
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

``` python
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        degree_list = [0] * numCourses
        pre_list = [[] for i in xrange(numCourses)]
        for x, y in prerequisites:
            degree_list[x] += 1
            pre_list[y].append(x)
        stack = [index for index, i in enumerate(degree_list) if i == 0]
        while stack:
            curr = stack.pop()
            numCourses -= 1
            for j in pre_list[curr]:
                degree_list[j] -= 1
                if degree_list[j] == 0:
                    stack.append(j)
        return numCourses == 0
```
