---
layout: post
title: Find the Weak Connected Component in the Directed Graph
date: 2015-10-21 14:42:25.000000000 -04:00
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
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468261482;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1949;}i:1;a:1:{s:2:"id";i:434;}i:2;a:1:{s:2:"id";i:476;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Find the number Weak Connected Component in the directed graph. Each node in the graph contains a label and a list of its neighbors. (a connected set of a directed graph is a subgraph in which any two vertices are connected by direct edge path.)</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param nodes a array of Directed graph node
     * @return a connected set of a directed graph
     */
     
    class UnionFind {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        public int find(int a) {
            if (!map.containsKey(a)) {
                map.put(a, a);
                return a;
            }
            int copy = a;
            while (copy != map.get(copy)) {
                copy = map.get(copy);
            }
            while (a != map.get(a)) {
                int temp = map.get(a);
                map.put(a, copy);
                a = temp;
            }
            return a;
        }
    }
    public List<List<integer>> connectedSet2(ArrayList<directedgraphnode> nodes) {
        // Write your code here
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (nodes == null || nodes.size() == 0) return result;
        
        UnionFind uf = new UnionFind();
        for (DirectedGraphNode node : nodes) {
            for (DirectedGraphNode neighbor : node.neighbors) {
                int father = uf.find(node.label);
                int son = uf.find(neighbor.label);
                uf.map.put(father, son);
            }
        }
        
        HashMap<Integer, List<integer>> graph = new HashMap<Integer, List<integer>>();
        for (DirectedGraphNode node : nodes) {
            List<integer> list = new ArrayList<integer>();
            int root = uf.find(node.label);
            if (graph.containsKey(root)) {
                list = graph.get(root);
            }
            list.add(node.label);
            graph.put(root, list);
        }
        
        for (int key : graph.keySet()) {
            result.add(graph.get(key));
        }
        return result;
    }
}
</integer></integer></integer></integer></integer></integer></directedgraphnode></integer></pre>
<p>[/expand]</p>
