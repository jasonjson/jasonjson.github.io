---
layout: post
title: Count Univalue Subtrees
date: 2015-11-02 08:49:03.000000000 -05:00
tags:
- Algorithm
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary tree, count the number of uni-value subtrees. A Uni-value subtree means all nodes of the subtree have the same value with the root.</em></strong></p>


``` java
public class Solution {
    public int countUnivalSubtrees(TreeNode root) {
        if (root == null) return 0;
        //if (root.left == null && root.right == null) return 1;
        int result = countUnivalSubtrees(root.left) + countUnivalSubtrees(root.right);
        if (isUnival(root)) result += 1;
        return result;
        
    }
    
    public boolean isUnival(TreeNode root) {
        if (root == null) return true;
        //if (root.left == null && root.right == null) return true;
        if (root.left != null && root.left.val != root.val) return false;
        if (root.right != null && root.right.val != root.val) return false;
        return isUnival(root.left) && isUnival(root.right);
    }
}
```
