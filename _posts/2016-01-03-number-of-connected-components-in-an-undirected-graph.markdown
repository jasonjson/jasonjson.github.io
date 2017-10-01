---
layout: post
title: Number of Connected Components in an Undirected Graph
date: 2016-01-03 19:50:36.000000000 -05:00
tags:
- Leetcode
categories:
- BFS
- Data Structure
author: Jason
---
<p><strong><em>Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.</em></strong></p>


``` java
public class Solution {
    class UnionFind {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        public int find(int x) {
            if (!map.containsKey(x)) {
                map.put(x, x);
                return x;
            }
            int y = x;
            while (y != map.get(y)) {
                y = map.get(y);
            }
            while (x != map.get(x)) {
                int temp = map.get(x);
                map.put(x, y);
                x = temp;
            }
            return x;
        }
    }
    public int countComponents(int n, int[][] edges) {
        UnionFind uf = new UnionFind();
        for (int[] edge : edges) {
            int father1 = uf.find(edge[0]);
            int father2 = uf.find(edge[1]);
            if (father1 != father2) {
                n--;
                uf.map.put(father1, father2);
            }
        }
        return n;
    }
}
```
``` java
public class Solution {
    public int countComponents(int n, int[][] edges) {
        if (n == 0) return 0;
        List<List<Integer>> neighbors = new ArrayList<List<Integer>>();
        for (int i = 0; i < n; i++) {
            neighbors.add(new ArrayList<Integer>());
        }
        for (int[] edge : edges) {
            neighbors.get(edge[0]).add(edge[1]);
            neighbors.get(edge[1]).add(edge[0]);
        }
        int count = 0;
        Queue<Integer> q = new LinkedList<Integer>();
        boolean[] visited = new boolean[n];
        q.offer(0);
        visited[0] = true;
        while (!q.isEmpty()) {
            int curr = q.poll();
            for (int neighbor : neighbors.get(curr)) {
                if (!visited[neighbor]) {
                    q.offer(neighbor);
                    visited[neighbor] = true;
                }
            }
            if (q.isEmpty()) {
                count++;
                for (int i = 0; i < n; i++) {
                    if (!visited[i]) {
                        q.offer(i);
                        visited[i] = true;
                        break;
                    }
                }
            }
        }
        return count;
    }
}
```
