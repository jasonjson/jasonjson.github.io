---
layout: post
title: 543 - Diameter of a Binary Tree
date: 2015-10-21 02:54:43.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.**


``` java
class Solution {
    public int diameter(TreeNode root) {
        if (root == null) return 0;

        int leftHeight = getHeight(root.left);
        int rightHeight = getHeight(root.right);
        int leftDia = diameter(root.left);
        int rightDia = diameter(root.right);

        return Math.max(Math.max(leftDia, rightDia), leftHeight + rightHeight);
        //the maximum diameter might path the root, or on the left subtree, or in the right subtree
    }

    public int getHeight(TreeNode root) {
        if (root == null) return 0;
        return Math.max(getHeight(root.left), getHeight(root.right)) + 1;
    }
};
```

``` python
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), self.get_depth(root.left) + self.get_depth(root.right))

    def get_depth(self, root):
        if not root:
            return 0
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1
```
