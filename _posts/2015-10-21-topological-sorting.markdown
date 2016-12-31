---
layout: post
title: Topological Sorting
date: 2015-10-21 12:56:31.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464652763;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:591;}i:1;a:1:{s:2:"id";i:1949;}i:2;a:1:{s:2:"id";i:476;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an directed graph, a topological order of the graph nodes is defined as follow: For each directed edge A -> B in graph, A must before B in the order list. The first node in the order can be any node in the graph with no nodes direct to it. Find any topological order for the given graph.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public ArrayList<directedgraphnode> topSort(ArrayList<directedgraphnode> graph) {
        ArrayList<directedgraphnode> result = new ArrayList<directedgraphnode>();
        if (graph == null || graph.size() == 0) return result;
        
        HashMap<DirectedGraphNode, Integer> map = new HashMap<DirectedGraphNode, Integer>();        
        for (DirectedGraphNode node : graph) {
            for (DirectedGraphNode neighbor : node.neighbors) {
                if (map.containsKey(neighbor)) {
                    map.put(neighbor, map.get(neighbor) + 1);
                } else {
                    map.put(neighbor, 1);
                }
            }
        }
        for (DirectedGraphNode node : graph) {
            if (!map.containsKey(node)) {
                dfs(node, map, result);
            }
        }
        return result;
    }    
    public void dfs(DirectedGraphNode node,  HashMap<DirectedGraphNode, Integer> map, ArrayList<directedgraphnode> result) {
        result.add(node);
        for (DirectedGraphNode neighbor : node.neighbors) {
            map.put(neighbor, map.get(neighbor) - 1);
            if (map.get(neighbor) == 0) {
                dfs(neighbor, map, result);
            }
        }
    }
}//DFS
</directedgraphnode></directedgraphnode></directedgraphnode></directedgraphnode></directedgraphnode></pre>
<pre>
public class Solution {
    /**
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */    
    public ArrayList<directedgraphnode> topSort(ArrayList<directedgraphnode> graph) {
        ArrayList<directedgraphnode> result = new ArrayList<directedgraphnode>();
        if (graph == null || graph.size() == 0) return result;
        
        HashMap<DirectedGraphNode, Integer> map = new HashMap<DirectedGraphNode, Integer>();
        
        for (DirectedGraphNode node : graph) {
            for (DirectedGraphNode neighbor : node.neighbors) {
                if (map.containsKey(neighbor)) {
                    map.put(neighbor, map.get(neighbor) + 1);
                } else {
                    map.put(neighbor, 1);
                }
            }
        }
        
        Queue<directedgraphnode> queue = new LinkedList<directedgraphnode>();
        for (DirectedGraphNode node : graph) {
            if (!map.containsKey(node)) {
                queue.add(node);
            }
        }
        while (!queue.isEmpty()) {
            DirectedGraphNode node = queue.poll();
            result.add(node);
            for (DirectedGraphNode neighbor : node.neighbors) {
                map.put(neighbor, map.get(neighbor) - 1);
                if (map.get(neighbor) == 0) {
                    queue.add(neighbor);
                }
            }
        }
        return result;
    }
}//BFS
</directedgraphnode></directedgraphnode></directedgraphnode></directedgraphnode></directedgraphnode></directedgraphnode></pre>
<p>[/expand]</p>
