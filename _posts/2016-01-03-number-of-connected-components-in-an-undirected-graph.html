---
layout: post
title: Number of Connected Components in an Undirected Graph
date: 2016-01-03 19:50:36.000000000 -05:00
type: post
published: true
status: publish
categories:
- BFS
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469283843;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:591;}i:1;a:1:{s:2:"id";i:302;}i:2;a:1:{s:2:"id";i:547;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.</em></strong></p>
<p>[expand title="Union Find"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
<p>[expand title="BFS"]</p>
<pre>
public class Solution {
    public int countComponents(int n, int[][] edges) {
        if (n == 0) return 0;
        List<List<integer>> neighbors = new ArrayList<List<integer>>();
        for (int i = 0; i < n; i++) {
            neighbors.add(new ArrayList<integer>());
        }
        for (int[] edge : edges) {
            neighbors.get(edge[0]).add(edge[1]);
            neighbors.get(edge[1]).add(edge[0]);
        }
        int count = 0;
        Queue<integer> q = new LinkedList<integer>();
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
</integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
