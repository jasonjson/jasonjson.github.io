---
layout: post
title: Binary Tree Maximum Path Sum
date: 2015-10-21 02:52:23.000000000 -04:00
tags:
- Algorithm
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.</em></strong></p>


``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: An integer.
     */
    
    public static int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        if (root == null) return 0;
        helper(root);
        return max;
    }
    public int helper(TreeNode root) {
        if (root == null) return 0;
        int leftMax = helper(root.left);
        int rightMax = helper(root.right);
        int arch = root.val + leftMax + rightMax;
        // 表示通过root节点能走到root的parent的最大和，这个值作为返回对象返给调用父函数  
        // 只有3中情况: 1 从左子树到root再到parent  
        // 2 从右子树到root再到parent  
        // 3 直接从root到parent  
        // 注意arch那条路是不可能走到parent，因为那条路已经经过root了，除非折回来重复走！但这是不允许的 
        int localMax = Math.max(root.val, Math.max(leftMax, rightMax) + root.val);
        // max 保存在所有递归过程中的最大值，这时也要考虑arch可能最大
        max = Math.max(max, Math.max(localMax, arch));
        return localMax;
    }
}
```
