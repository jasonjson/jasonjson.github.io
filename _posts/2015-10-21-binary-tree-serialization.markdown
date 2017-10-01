---
layout: post
title: Binary Tree Serialization
date: 2015-10-21 02:57:07.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
- Data Structure
author: Jason
---
<p><strong><em>Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.</em></strong></p>


``` java
class Solution {
    public String serialize(TreeNode root) {
        StringBuilder str = new StringBuilder();
        if (root == null) return str.toString();
        serializeHelper(root, str);
        return str.toString();
    }
    
    public void serializeHelper(TreeNode root, StringBuilder str) {
        if (root == null) {
            str.append("#.");
        } else {
            str.append(root.val + ".");
            serializeHelper(root.left, str);
            serializeHelper(root.right, str);
        }
    }

    public TreeNode deserialize(String data) {
        if (data == null || data.length() == 0) return null;
        String[] strs = data.split(".");
        int[] index = new int[] {0};
        return deserializeHelper(strs, index);
    }
    
    public TreeNode deserializeHelper(String[] strs, int[] index) {
        if (index[0] == strs.length) return null;
        String next = strs[index[0]++];
        if (next.equals("#")) {
            return null;
        } else {
            TreeNode root = new TreeNode(Integer.valueOf(next));
            root.left = deserializeHelper(strs, index);
            root.right = deserializeHelper(strs, index);
            return root;
        }
    }
}
```
