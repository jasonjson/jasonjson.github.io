---
layout: post
title: 310 - Minimum Height Trees
date: 2015-11-26 15:18:26.000000000 -05:00
tags:
- Leetcode
categories:
- Graph
author: Jason
---
**For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.**


``` java
public class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Integer> result = new ArrayList<>();
        if (n == 1) {
            result.add(0);
            return result;
        }

        int[] degrees = new int[n];
        List<List<Integer>> neighbors = new ArrayList<List<Integer>>();
        for (int i = 0; i < n; i++) {
            neighbors.add(new ArrayList<Integer>());
        }
        for (int[] edge : edges) {
            degrees[edge[0]] ++;
            degrees[edge[1]] ++;
            neighbors.get(edge[0]).add(edge[1]);
            neighbors.get(edge[1]).add(edge[0]);
        }

        List<Integer> preLevel = new ArrayList<Integer>();
        for (int i = 0; i < degrees.length; i++) {
            if (degrees[i] == 1) {
                preLevel.add(i);
            }
        }
        while (preLevel.size() > 1) {//the number of roots can be at most 2
            List<Integer> currLevel = new ArrayList<>();
            for (int point : preLevel) {
                for (int next : neighbors.get(point)) {
                    degrees[next]--;
                    if (degrees[next] == 1) {
                        currLevel.add(next);
                    }
                }
            }
            if (currLevel.size() == 0) return preLevel;//the number of roots are 2
            preLevel = currLevel;
        }
        return preLevel;
    }
}
```

``` python
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        edge_map = collections.defaultdict(list)
        for a, b in edges:
            edge_map[a].append(b)
            edge_map[b].append(a)

        prev = [k for k, v in edge_map.iteritems() if len(v) == 1]
        while len(prev) >= 2:
            curr = []
            for a in prev:
                for neighbor in edge_map[a]:
                    edge_map[neighbor].remove(a)
                    if len(edge_map[neighbor]) == 1:
                        curr.append(neighbor)
            if len(curr) == 0:
                return prev
            else:
                prev = curr
        return prev
```
