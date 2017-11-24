---
layout: post
title: 99 - Recover Binary Search Tree
date: 2015-11-11 17:51:55.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Two elements of a binary search tree (BST) are swapped by mistake. Recover the tree without changing its structure.**


``` java
public class Solution {
    private TreeNode n1 = null, n2 = null, prev = null;
    public void recoverTree(TreeNode root) {
        if (root == null) return;
        recover(root);
        int temp = n1.val;
        n1.val = n2.val;
        n2.val = temp;
    }
    public void recover(TreeNode root) {
        if (root == null) return;
        recover(root.left);
        if (prev != null && prev.val > root.val) {
            if (n1 == null) {
                n1 = prev;
            }
            n2 = root;
        }
        prev = root;
        recover(root.right);
    }
}
```

``` python
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        first = prev = second = None
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if prev is not None and root.val < prev.val:
                    if first is None:
                        first = prev
                    second = root
                prev = root
                root = root.right
        first.val, second.val = second.val, first.val
```
