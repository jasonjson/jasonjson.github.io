---
layout: post
title: Binary Tree Right Side View
date: 2015-11-04 15:49:10.000000000 -05:00
tags:
- Algorithm
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.</em></strong></p>


``` java
public class Solution { //level order traversal
    public List<integer> rightSideView(TreeNode root) {
        List<integer> result = new ArrayList<integer>();
        if (root == null) return result;
        
        Queue<treenode> q = new LinkedList<treenode>();
        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                if (i == size - 1) {
                    result.add(curr.val);
                }
                if (curr.left != null) q.offer(curr.left);
                if (curr.right != null) q.offer(curr.right);
            }
        }
        return result;
    }
}
```
