---
layout: post
title: 116 - Populating Next Right Pointers in Each Node
date: 2015-11-09 17:36:58.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. Initially, all next pointers are set to NULL.**


``` java
public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null || (root.left == null && root.right == null)) return;
        root.left.next = root.right;
        if (root.next != null) root.right.next = root.next.left;
        connect(root.left);
        connect(root.right);
    }
}
```

``` python
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root or not root.left or root.right:
            return

        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        connect(root.left)
        connect(root.right)
```
