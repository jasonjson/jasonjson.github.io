---
layout: post
title: 230 - Kth Smallest Element in a BST
date: 2015-11-02 18:05:03.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.**


``` java
public class Solution {
    public int kthSmallest(TreeNode root, int k) {
        if (root == null || k <= 0) return -1;
        Stack<treenode> stack = new Stack<treenode>();
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (k-- == 1) return root.val;
                root = root.right;
            }
        }
        return -1;
    }
}
```

``` python
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        if not root:
            return -1

        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                k -= 1
                if k == 0:
                    return root.val
                root = root.right
        return -1
```
