---
layout: post
title: 110 - Balanced Binary Tree
date: 2015-10-21 02:51:52.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, determine if it is height-balanced. For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.**


``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if this Binary tree is Balanced, or false.
     */
    public boolean isBalanced(TreeNode root){
        return getHeight(root) != -1;

    }

    public int getHeight(TreeNode root){
        if (root == null) return 0;

        int left = getHeight(root.left);
        int right = getHeight(root.right);
        if (left == -1 || right == -1 || Math.abs(left - right) > 1) {
            return -1;
        }
        return Math.max(left, right) + 1;
    }
}
```

``` python
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.get_depth(root) != -1

    def get_depth(self, root):
        if root is None:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1
```
