---
layout: post
title: Binary Tree Postorder Traversal
date: 2015-10-21 02:50:25.000000000 -04:00
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Binary tree postorder traversal</em></strong></p>


``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: Postorder in ArrayList which contains node values.
     */
    public ArrayList<integer> postorderTraversal(TreeNode root) {
        // write your code here
        ArrayList<integer> result = new ArrayList<integer>();
        if (root == null) return result;
        
        Stack<treenode> stack = new Stack<treenode>();
        TreeNode prev = null;
        stack.push(root);
        while (!stack.isEmpty()) {
            root = stack.peek();
            boolean nochildren = false;
            if (root.left == null && root.right == null) {
                nochildren = true;
            }
            boolean childrenvisited = false;
            if (prev != null && (root.left == prev || root.right == prev)) {
                childrenvisited = true;
            }
            if (nochildren || childrenvisited) {
                prev = stack.pop();
                result.add(root.val);
            } else {
                if (root.right != null) {
                    stack.push(root.right);
                }
                if (root.left != null) {
                    stack.push(root.left);
                }
            }
        }
        return result;
    }
}
```
``` java
public class Solution {
    public ArrayList<integer> postorderTraversal(TreeNode root) {
        // write your code here
        ArrayList<integer> result = new ArrayList<integer>();
        if (root != null) {
            ArrayList<integer> left = postorderTraversal(root.left);
            ArrayList<integer> right = postorderTraversal(root.right);
            result.addAll(left);
            result.addAll(right);
            result.add(root.val);
        }
        return result;
    }
}
```
