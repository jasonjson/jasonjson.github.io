---
layout: post
title: Binary Tree Maximum Path Sum
date: 2015-10-21 02:52:23.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468937457;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1058;}i:1;a:1:{s:2:"id";i:1424;}i:2;a:1:{s:2:"id";i:1146;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.</em></strong><br />
[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
