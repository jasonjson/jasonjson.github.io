---
layout: post
title: Topological Sorting
date: 2015-10-21 12:56:31.000000000 -04:00
tags:
- Algorithm
categories:
- Graph
author: Jason
---
<p><strong><em>Given an directed graph, a topological order of the graph nodes is defined as follow: For each directed edge A -> B in graph, A must before B in the order list. The first node in the order can be any node in the graph with no nodes direct to it. Find any topological order for the given graph.</em></strong></p>


``` java
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
```
``` java
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
```
