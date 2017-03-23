---
layout: post
title: Course Schedule
date: 2015-11-04 12:41:18.000000000 -05:00
tags:
- Algorithm
categories:
- Graph
- Sorting
author: Jason
---
<p><strong><em>There are a total of n courses you have to take, labeled from 0 to n - 1.</p>

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]</p>
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?</em></strong></p>
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
