---
layout: post
title: 545 - Boundary Of Binary Tree
date: 2020-02-01
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

```python
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ret = [root.val]
        def get_left(curr):
            if not curr or (not curr.left and not curr.right):
                return
            ret.append(curr.val)
            get_left(curr.left) if curr.left else get_left(curr.right)
        def get_right(curr):
            if not curr or (not curr.left and not curr.right):
                return
            get_right(curr.right) if curr.right else get_right(curr.left)
            ret.append(curr.val)

        def get_leaf(curr):
            if not curr:
                return
            elif not curr.left and not curr.right:
                ret.append(curr.val)
            else:
                get_leaf(curr.left)
                get_leaf(curr.right)

        get_left(root.left)
        get_leaf(root.left)
        get_leaf(root.right)
        get_right(root.right)
        return ret
```
