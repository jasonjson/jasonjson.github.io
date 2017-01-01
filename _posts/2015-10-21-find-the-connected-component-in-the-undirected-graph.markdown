---
layout: post
title: Find the Connected Component in the Undirected Graph
date: 2015-10-21 12:55:02.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465899524;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:591;}i:1;a:1:{s:2:"id";i:1949;}i:2;a:1:{s:2:"id";i:434;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its neighbors. (a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param nodes a array of Undirected graph node
     * @return a connected set of a Undirected graph
     */
    public List<List<integer>> connectedSet(ArrayList<undirectedgraphnode> nodes) {
        // Write your code here
        List<List<integer>> result = new ArrayList<List<integer>>();
        //if (nodes == null || nodes.size() == 0) return result;
        
        HashMap<UndirectedGraphNode, Boolean> visited = new HashMap<UndirectedGraphNode, Boolean>();
        for (UndirectedGraphNode node : nodes) {
            visited.put(node, false);
        }
        for (UndirectedGraphNode node : nodes) {
            if (!visited.get(node)) {
                result.add(bfs(node, visited));
            }
        }
        return result;
    }
    
    public List<integer> bfs(UndirectedGraphNode node, HashMap<UndirectedGraphNode, Boolean> visited) {
        List<integer> list = new ArrayList<integer>();
        LinkedList<undirectedgraphnode> q = new LinkedList<undirectedgraphnode>();
        q.add(node);
        visited.put(node, true);
        while (!q.isEmpty()) {
            node = q.poll();
            list.add(node.label);
            for (UndirectedGraphNode neighbor : node.neighbors) {
                if (!visited.get(neighbor)) {
                    q.add(neighbor);
                    visited.put(neighbor, true);
                }
            }
        }
        Collections.sort(list);
        return list;
    }
}
</undirectedgraphnode></undirectedgraphnode></integer></integer></integer></integer></integer></undirectedgraphnode></integer></pre>
<p>[/expand]</p>
