---
layout: post
title: 951 - Flip Equivalent Binary Trees
date: 2020-02-05
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees. A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations. Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

```python
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return root1 == root2
        return root1.val == root2.val and (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        q1, q2 = [root1], [root2]
        while q1 and q2:
            r1, r2 = q1.pop(0), q2.pop(0)
            if not r1 and not r2:
                continue
            if not r1 or not r2 or r1.val != r2.val:
                return False
            if r1.left == r2.left or r1.left and r2.left and r1.left.val == r2.left.val:
                q1.extend([r1.left, r1.right])
            else:
                q1.extend([r1.right, r1.left])
            q2.extend([r2.left, r2.right])
        return not q1 and not q2
```
