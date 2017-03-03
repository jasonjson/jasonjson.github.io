---
layout: post
title: Binary Tree Level Order Traversal
date: 2015-10-21 02:50:43.000000000 -04:00
tags: algorithm
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Binary tree level order traversal</em></strong></p>


``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: Level order a list of lists of integer
     */
     public ArrayList<ArrayList<integer>> levelOrder(TreeNode root){
         ArrayList<ArrayList<integer>> result = new ArrayList<ArrayList<integer>>();
         if (root == null) return result;
         
         Queue<treenode> q = new LinkedList<treenode>();
         q.add(root);
         while (!q.isEmpty()) {
            int size = q.size();
            //control when the level ends
            ArrayList<integer> list = new ArrayList<integer>();
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                list.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            result.add(list);
         }
         return result;
     }
}
```
