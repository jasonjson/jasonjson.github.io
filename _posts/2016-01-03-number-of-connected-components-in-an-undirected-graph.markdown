---
layout: post
title: 323 - Number of Connected Components in an Undirected Graph
date: 2016-01-03 19:50:36.000000000 -05:00
tags:
- Leetcode
categories:
- Graph
author: Jason
---
**Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.**


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

``` python
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n == 0:
            return 0

        visited = [False] * n
        neighbors = collections.defaultdict(list)
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        ret = 0
        queue = collections.deque([0])
        visited[0] = True
        while queue:
            curr = queue.popleft()
            for neighbor in neighbors[curr]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
            if not queue:
                ret += 1
                for i in xrange(n):
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True
                        break
        return ret
```
