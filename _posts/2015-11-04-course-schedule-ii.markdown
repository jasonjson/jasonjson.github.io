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
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses:
            return []

        course_map = defaultdict(list)
        course_depth = {i: 0 for i in range(numCourses)}

        for a, b in prerequisites:
            course_map[b].append(a)
            course_depth[a] += 1
        ret = []
        queue = [c for c in course_depth if course_depth[c] == 0]
        while queue:
            curr = queue.pop(0)
            ret.append(curr)
            for next_one in course_map[curr]:
                course_depth[next_one] -= 1
                if course_depth[next_one] == 0:
                    queue.append(next_one)
        return ret if len(ret) == numCourses else []
```
