---
layout: post
title: Sum Root to Leaf Numbers
date: 2015-11-06 22:04:46.000000000 -05:00
tags:
- Algorithm
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.</p>

An example is the root-to-leaf path 1->2->3 which represents the number 123.</p>
Find the total sum of all root-to-leaf numbers.</em></strong></p>
``` java
public class Solution {
    public int sumNumbers(TreeNode root) {
        if (root == null) return 0;
        
        List<string> result = new ArrayList<string>();
        helper(root, "", result);
        int sum = 0;
        for (String s : result) {
            sum += Integer.parseInt(s);
        }
        return sum;
    }
    
    public void helper(TreeNode root, String path, List<string> result) {
        if (root == null) {
            return;
        }
        if (root.left == null && root.right == null) {
            result.add(new String(path + String.valueOf(root.val)));
        }
        helper(root.left, path + String.valueOf(root.val), result);
        helper(root.right, path + String.valueOf(root.val), result);
    }
}
```
