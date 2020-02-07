---
layout: post
title: 987 - Vertical Order Traversal Of A Binary Tree
date: 2020-02-06
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
Given a binary tree, return the vertical order traversal of its nodes values. For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1). Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates). If two nodes have the same position, then the value of the node that is reported first is the value that is smaller. Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

```python
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [(root, 0, 0)]
        node_dict = defaultdict(list)
        while queue:
            curr, h, v = queue.pop() #horizontal, vertical index
            node_dict[h].append((v, curr.val))
            if curr.left:
                queue.append((curr.left, h - 1, v + 1))
            if curr.right:
                queue.append((curr.right, h + 1, v + 1))

        return [[a[1] for a in sorted(v)] for _, v in sorted(node_dict.items())]
```
