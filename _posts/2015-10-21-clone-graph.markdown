---
layout: post
title: Clone Graph
date: 2015-10-21 13:25:04.000000000 -04:00
tags:
- Algorithm
categories:
- Graph
author: Jason
---
<p><strong><em>Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.</em></strong></p>


``` java
public class Solution {
    HashMap<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        // write your code here
        if (node == null) return null;
        UndirectedGraphNode newNode = new UndirectedGraphNode(node.label);
        map.put(node, newNode);
        for (UndirectedGraphNode neighbor : node.neighbors) {
            if (!map.containsKey(neighbor)) {
                UndirectedGraphNode newNeighbor = cloneGraph(neighbor);
                map.put(neighbor, newNeighbor);
            }
            newNode.neighbors.add(map.get(neighbor));
        }
        return newNode;
    }
}
```
``` java
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) return null;        
        HashMap<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
        Queue<undirectedgraphnode> queue = new LinkedList<undirectedgraphnode>();        
        UndirectedGraphNode newNode = new UndirectedGraphNode(node.label);
        map.put(node, newNode);
        queue.add(node);//always add old node for cloning
        while (!queue.isEmpty()) {
            UndirectedGraphNode curr = queue.poll();
            UndirectedGraphNode newCurr = map.get(curr);
            for (UndirectedGraphNode neighbor : curr.neighbors) {
                if (map.containsKey(neighbor)) {
                    newCurr.neighbors.add(map.get(neighbor));
                } else {
                    UndirectedGraphNode newNeighbor = new UndirectedGraphNode(neighbor.label);
                    newCurr.neighbors.add(newNeighbor);
                    map.put(neighbor, newNeighbor);
                    queue.add(neighbor);//neighbor might have neighbors, push it to queue
                }
            }
        }
        return newNode;
    }
```
