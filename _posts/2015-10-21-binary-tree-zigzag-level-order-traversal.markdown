---
layout: post
title: Binary Tree Zigzag Level Order Traversal
date: 2015-10-21 02:56:43.000000000 -04:00
tags: algorithm
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).</em></strong></p>


``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: A list of lists of integer include 
     *          the zigzag level order traversal of its nodes' values 
     */
    public ArrayList<ArrayList<integer>> zigzagLevelOrder(TreeNode root) {
        // write your code here
        ArrayList<ArrayList<integer>> result = new ArrayList<ArrayList<integer>>();
        if (root == null) return result;
        
        Queue<treenode> q = new LinkedList<treenode>();
        q.add(root);
        boolean even = true;
        while (!q.isEmpty()) {
            int size = q.size();
            ArrayList<integer> list = new ArrayList<integer> ();
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                list.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            if (even) {
                result.add(list);
            } else {
                Collections.reverse(list);
                result.add(list);
            }
            even = !even;
        }
        return result;
    }
}
```
