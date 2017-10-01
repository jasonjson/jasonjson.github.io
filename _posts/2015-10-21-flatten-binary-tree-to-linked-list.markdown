---
layout: post
title: 114 - Flatten Binary Tree to Linked List
date: 2015-10-21 14:43:36.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, flatten it to a linked list in-place.**


``` java
public class Solution {
    public void flatten(TreeNode root) {
        if (root == null) return;

        Stack<treenode> stack = new Stack<treenode>();
        stack.push(root);
        TreeNode prev = null;
        while (!stack.isEmpty()) {
            TreeNode curr = stack.pop();
            if (prev != null) {
                prev.right = curr;
                prev.left = null;
            }
            prev = curr;
            if (curr.right != null) {
                stack.push(curr.right);
            }
            if (curr.left != null) {
                stack.push(curr.left);
            }
        }
    }
}
```
``` java
public class Solution {
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void flatten(TreeNode root) {
        // write your code here
        if (root == null) return;
        helper(root);
    }
    public TreeNode helper(TreeNode root) {
        if (root == null) return null;
        TreeNode left = helper(root.left);
        TreeNode right = helper(root.right);
        root.left = null;
        root.right = left;
        TreeNode curr = root;
        while (curr.right != null) {
            curr = curr.right;
        }
        curr.right = right;
        return root;
    }
}
```

``` python
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = [root]
        prev = None
        while stack:
            curr = stack.pop()
            if prev:
                prev.right = curr
                prev.left = None
            prev = curr
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
```
