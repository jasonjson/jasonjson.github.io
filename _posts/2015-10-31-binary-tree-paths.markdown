---
layout: post
title: Binary Tree Paths
date: 2015-10-31 11:01:44.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary tree, return all root-to-leaf paths.</em></strong></p>


``` java
public class Solution {
    public List<string> binaryTreePaths(TreeNode root) {
        List<string> result = new ArrayList<string>();
        if (root == null) return result;
        helper(root, "", result);
        return result;
    }
    
    public void helper(TreeNode root, String path, List<string> result) {
        if (root.left == null && root.right == null) {
            result.add(new String(path + root.val));//leaf node必须单独处理
            return;
        }
        if (root.left != null) helper(root.left, path + root.val + "->" , result);
        if (root.right != null) helper(root.right, path + root.val + "->", result);
    }
}
```
