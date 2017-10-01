---
layout: post
title: Binary Tree Preorder Traversal
date: 2015-10-21 02:49:50.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Preorder traversal a binary tree</em></strong></p>


``` java
public class Solution {
    public List<integer> preorderTraversal(TreeNode root) {
        List<integer> result = new ArrayList<integer>();
        if (root != null) {
            List<integer> left = preorderTraversal(root.left);
            List<integer> right = preorderTraversal(root.right);
            result.add(root.val);
            result.addAll(left);
            result.addAll(right);
        }
        return result;
    }
    //iterative!
    public ArrayList<integer> preorderTraversal(TreeNode root) {
        // write your code here
        ArrayList<integer> result = new ArrayList<integer>();
        if (root == null) {
            return result;
        }
        Stack<treenode> stack = new Stack<treenode>();
        stack.push(root);
        while (!stack.isEmpty()){
            TreeNode node = stack.pop();
            result.add(node.val); 
            //push right node first, which comes out later
            if (node.right != null) stack.push(node.right);
            if (node.left != null) stack.push(node.left);
        }
        return result;
    }
}
```
