---
layout: post
title: Closest Binary Search Tree Value II
date: 2015-10-30 11:29:11.000000000 -04:00
tags:
- Algorithm
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.</em></strong></p>

Note:</p>
Given target value is a floating point.</p>
You may assume k is always valid, that is: k ≤ total nodes.</p>
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.</p>
<p>Follow up:</p>
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)? Divide and conquer, get the result from left subtree and right subtree then merge</p>
``` java
public class Solution {
    public List<integer> closestKValues(TreeNode root, double target, int k) {
        List<integer> result = new ArrayList<integer>();
        if (root == null) return result;
        
        Stack<treenode> stack = new Stack<treenode>();
        while (!stack.isEmpty() || root != null) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (result.size() < k) {
                    result.add(root.val);
                } else if (Math.abs(root.val - target) < Math.abs(result.get(0) - target)) {
                    result.remove(0);
                    result.add(root.val);
                } else {//后面的数更大 不需要考虑 关键是找到中间k个数
                    break;
                }
                root = root.right;
            }
        }
        return result;
    }
}
```
