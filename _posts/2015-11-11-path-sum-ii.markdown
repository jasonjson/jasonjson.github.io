---
layout: post
title: Path Sum II
date: 2015-11-11 09:05:32.000000000 -05:00
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.</em></strong></p>


``` java
public class Solution {
    public List<List<integer>> pathSum(TreeNode root, int sum) {
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (root == null) return result;
        helper(root, new ArrayList<integer>(), sum, result);
        return result;
    }
    
    public void helper(TreeNode root, List<integer> path, int remain, List<List<integer>> result) {
        if (root == null) return;
        path.add(root.val);
        if (root.left == null && root.right == null && root.val == remain) {
            result.add(new ArrayList<integer>(path));//加进result的条件比较特殊,必须到了leaf且leaf的值等于remain
        }
        helper(root.left, path, remain - root.val, result);
        helper(root.right, path, remain - root.val, result);
        path.remove(path.size() - 1);
    }
}
```
