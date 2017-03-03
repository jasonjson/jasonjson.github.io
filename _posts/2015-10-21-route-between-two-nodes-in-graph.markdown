---
layout: post
title: Route Between Two Nodes in Graph
date: 2015-10-21 12:55:45.000000000 -04:00
tags: algorithm
categories:
- Graph
author: Jason
---
<p><strong><em>Given a directed graph, design an algorithm to find out whether there is a route between two nodes.</em></strong></p>


``` java
public class Solution {
   /**
     * @param graph: A list of Directed graph node
     * @param s: the starting Directed graph node
     * @param t: the terminal Directed graph node
     * @return: a boolean value
     */
     
    public boolean hasRoute(ArrayList<directedgraphnode> graph, 
                            DirectedGraphNode s, DirectedGraphNode t) {
        if (graph == null || graph.size() == 0) return s == t;
        
        HashSet<directedgraphnode> visited = new HashSet<>();
        Queue<directedgraphnode> q = new LinkedList<directedgraphnode>();
        q.offer(s);
        visited.add(s);
        while (!q.isEmpty()) {
            DirectedGraphNode curr = q.poll();
            if (curr == t) return true;
            for (DirectedGraphNode neighbor : curr.neighbors) {
                if (!visited.contains(neighbor)) {
                    q.offer(neighbor);
                    visited.add(neighbor);
                }
            }
        }
        return false;
    }
}
```
