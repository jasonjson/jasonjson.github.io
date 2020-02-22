---
layout: post
title: 133 - Clone Graph
date: 2015-10-21 13:25:04.000000000 -04:00
tags:
- Leetcode
categories:
- Graph
author: Jason
---
**Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.**

``` python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        node_dict = {}
        new_node = Node(node.val)
        node_dict[node] = new_node
        queue = [node]
        while queue:
            curr = queue.pop(0)
            new_curr = node_dict.setdefault(curr, Node(curr.val))
            for neighbor in curr.neighbors:
                if neighbor not in node_dict:
                    node_dict[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                new_curr.neighbors.append(node_dict[neighbor])
        return new_node
```
