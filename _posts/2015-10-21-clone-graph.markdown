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
```python
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return

        new_node = UndirectedGraphNode(node.label)
        mapping = {node: new_node}
        queue = [node]
        while queue:
            curr = queue.pop()
            new_curr = mapping[curr]
            for neighbor in curr.neighbors:
                if neighbor not in mapping:
                    new_neighbor = UndirectedGraphNode(neighbor.label)
                    mapping[neighbor] = new_neighbor
                    queue.append(neighbor)
                new_curr.neighbors.append(mapping[neighbor])
        return new_node
```
