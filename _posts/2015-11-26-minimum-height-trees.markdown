---
layout: post
title: Minimum Height Trees
date: 2015-11-26 15:18:26.000000000 -05:00
categories:
- Brain teaser
- Graph
author: Jason
---
<p><strong><em>For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.</em></strong></p>


``` java
public class Solution {
    public List<integer> findMinHeightTrees(int n, int[][] edges) {
        List<integer> result = new ArrayList<>();
        if (n == 1) {
            result.add(0);
            return result;
        }
        
        int[] degrees = new int[n];
        List<List<integer>> neighbors = new ArrayList<List<integer>>();
        for (int i = 0; i < n; i++) {
            neighbors.add(new ArrayList<integer>());
        }
        for (int[] edge : edges) {
            degrees[edge[0]] ++;
            degrees[edge[1]] ++;
            neighbors.get(edge[0]).add(edge[1]);
            neighbors.get(edge[1]).add(edge[0]);
        }
        
        List<integer> preLevel = new ArrayList<integer>();
        for (int i = 0; i < degrees.length; i++) {
            if (degrees[i] == 1) {
                preLevel.add(i);
            }
        }
        while (preLevel.size() > 1) {//the number of roots can be at most 2
            List<integer> currLevel = new ArrayList<>();
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
