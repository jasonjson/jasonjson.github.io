---
layout: post
title: 863 - All Nodes Distance K In Binary Tree
date: 2020-01-21
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
We are given a binary tree (with root node root), a target node, and an integer value K. Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

```python
from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root or not target:
            return []
        conn = defaultdict(list)
        def helper(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child:
                helper(child, child.left)
                helper(child, child.right)
        helper(None, root)
        ret = [target.val]
        seen = set(ret)
        for _ in range(K):
            ret = [n for parent in ret for n in conn[parent] if n not in seen]
            seen |= set(ret)
        return ret
```
