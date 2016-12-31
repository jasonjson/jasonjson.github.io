---
layout: post
title: Course Schedule
date: 2015-11-04 12:41:18.000000000 -05:00
type: post
published: true
status: publish
categories:
- Graph
- Sorting
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463651971;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1326;}i:1;a:1:{s:2:"id";i:302;}i:2;a:1:{s:2:"id";i:1949;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>There are a total of n courses you have to take, labeled from 0 to n - 1.<br />
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]<br />
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
