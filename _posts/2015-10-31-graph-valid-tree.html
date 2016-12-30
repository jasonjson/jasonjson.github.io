---
layout: post
title: Graph Valid Tree
date: 2015-10-31 10:01:45.000000000 -04:00
type: post
published: true
status: publish
categories:
- Graph
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468740440;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1949;}i:1;a:1:{s:2:"id";i:1652;}i:2;a:1:{s:2:"id";i:1323;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.<br />
For example:<br />
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.<br />
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public boolean validTree(int n, int[][] edges) {
        List<Set<integer>> graph = new ArrayList<Set<integer>>();//构造graph的方法 adjacency list
        for (int i = 0; i < n; i++) {
            graph.add(new HashSet<integer>());
        }
        for (int i = 0; i < edges.length; i++) {
            graph.get(edges[i][0]).add(edges[i][1]);
            graph.get(edges[i][1]).add(edges[i][0]);
        }
        
        boolean[] visited = new boolean[n];
        Queue<integer> q = new LinkedList<integer>();
        q.offer(0);
        while (!q.isEmpty()) {
            int curr = q.poll();
            if (visited[curr]) {
                return false;
            }//遇到cycle
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
</integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
