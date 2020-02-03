---
layout: post
title: 1110 - Delete Nodes And Return Forest
date: 2020-02-02
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
Given the root of a binary tree, each node in the tree has a distinct value. After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees). Return the roots of the trees in the remaining forest.  You may return the result in any order.

```python
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ret = []
        def helper(curr, is_root):
            if not curr:
                return
            deleted = curr.val in to_delete
            if is_root and not deleted:
                ret.append(curr)
            curr.left = helper(curr.left, deleted)
            curr.right = helper(curr.right, deleted)
            return None if deleted else curr
        helper(root, True)
        return ret
```
