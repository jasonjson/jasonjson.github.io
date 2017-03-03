---
layout: post
title: Invert Binary Tree
date: 2015-10-21 02:53:24.000000000 -04:00
tags: algorithm
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Invert a binary tree</em></strong></p>


``` java
public class Solution {
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void invertBinaryTree(TreeNode root) {
        // write your code here
        if (root == null) return;
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        //from top to bottom
        invertBinaryTree(root.left);
        invertBinaryTree(root.right);
    }
}
```

``` java
public class Solution {
    //iterative
    public void invertBinaryTree(TreeNode root) {
        // write your code here
        if (root == null) return;
        Stack<treenode> stack = new Stack<treenode>();
        
        stack.push(root);
        while (!stack.isEmpty()) {
            //we don't care if the current level is finished, when i level is finished, it goes automatically to i + 1 level, root remain the same, because it's already swapped in the above level
            TreeNode curr = stack.pop();
            TreeNode temp = curr.left;
            curr.left = curr.right;
            curr.right = temp;
            if (curr.left != null)  stack.push(curr.left);
            if (curr.right != null) stack.push(curr.right);
        }
    }
}
```
