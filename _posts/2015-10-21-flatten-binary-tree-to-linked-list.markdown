---
layout: post
title: Flatten Binary Tree to Linked List
date: 2015-10-21 14:43:36.000000000 -04:00
categories:
- Binary Search Tree
- LinkedList
author: Jason
---
<p><strong><em>Flatten a binary tree to a fake "linked list" in pre-order traversal. Here we use the right pointer in TreeNode as the next pointer in ListNode.</em></strong></p>

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
