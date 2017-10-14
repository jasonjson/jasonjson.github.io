---
layout: post
title: 210 - Course Schedule II
date: 2015-11-04 12:59:54.000000000 -05:00
tags:
- Leetcode
categories:
- Graph
author: Jason
---
**There are a total of n courses you have to take, labeled from 0 to n - 1. Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1].  Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses. There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.**


``` java
public class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] result = new int[numCourses];
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
        int index = 0;
        while (!q.isEmpty()) {
            int curr = q.poll();
            numCourses--;
            result[index++] = curr;
            for (int next : course.get(curr)) {
                degree[next]--;
                if (degree[next] == 0) {
                    q.offer(next);
                }
            }
        }
        if (numCourses == 0) {
            return result;
        } else {
            return new int[]{};
        }
    }
}
```

``` python
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        degree_list = [0] * numCourses
        prere_list = [[] for i in xrange(numCourses)]
        for x, y in prerequisites:
            degree_list[x] += 1
            prere_list[y].append(x)
        ret = []
        stack = [index for index, i in enumerate(degree_list) if i == 0]
        while stack:
            curr = stack.pop()
            ret.append(curr)
            for j in prere_list[curr]:
                degree_list[j] -= 1
                if degree_list[j] == 0:
                    stack.append(j)
        return ret if len(ret) == numCourses else []
```
