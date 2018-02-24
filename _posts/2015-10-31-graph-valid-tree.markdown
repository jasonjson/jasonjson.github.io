---
layout: post
title: 261 - Graph Valid Tree
date: 2015-10-31 10:01:45.000000000 -04:00
tags:
- Leetcode
categories:
- Graph
author: Jason
---
**Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.**

**For example: Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true. Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.**


``` java
public class Solution {
    public boolean validTree(int n, int[][] edges) {
        List<Set<Integer>> graph = new ArrayList<Set<Integer>>();
        for (int i = 0; i < n; i++) {
            graph.add(new HashSet<Integer>());
        }
        for (int i = 0; i < edges.length; i++) {
            graph.get(edges[i][0]).add(edges[i][1]);
            graph.get(edges[i][1]).add(edges[i][0]);
        }

        boolean[] visited = new boolean[n];
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(0);
        while (!q.isEmpty()) {
            int curr = q.poll();
            if (visited[curr]) {
                return false;
            }
            visited[curr] = true;
            for (int neighbor : graph.get(curr)) {
                q.offer(neighbor);
                graph.get(neighbor).remove(curr);//去掉child - parent的边 后面不需再用
            }
        }
        for (boolean find : visited) {
            if (!find) {
                return false;
            }
        }
        return true;
    }
}
```

``` python
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        node_map = collections.defaultdict(list)
        for (a, b) in edges:
            node_map[a].append(b)
            node_map[b].append(a)

        queue = [0]
        visited = set()
        while queue:
            curr = queue.pop(0)
            if curr in visited:
                return False
            visited.add(curr)
            for neighbor in node_map[curr]:
                queue.append(neighbor)
                node_map[neighbor].remove(curr)
        return len(visited) == n
```
