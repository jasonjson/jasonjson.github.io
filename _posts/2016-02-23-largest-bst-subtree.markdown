---
layout: post
title: Largest BST Subtree
date: 2016-02-23 22:38:07.000000000 -05:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468948262;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1193;}i:1;a:1:{s:2:"id";i:1249;}i:2;a:1:{s:2:"id";i:1198;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int largestBSTSubtree(TreeNode root) {
        int[] result = helper(root);
        return result[1];
    }
    public int[] helper(TreeNode root) {
        int[] result = new int[5];
        //result[0]: is BST? result[2] : total number of nodes, result[3]: maximum value, result[4] minimum value
        result[0] = 1; result[3] = Integer.MIN_VALUE; result[4] = Integer.MAX_VALUE;
        if (root == null) return result;
        int[] result_left = helper(root.left);
        int[] result_right = helper(root.right);
        if (result_left[0] == 0 || result_right[0] == 0 || root.val >= result_right[4] || root.val <= result_left[3]) {
            result[0] = 0;
        }//root is larger than the biggest node in left subtree and smaller than smallest node in right subtree
        result[2] = result_left[2] + result_right[2] + 1;
        result[1] = result[0] == 1 ? result[2] : Math.max(result_left[1], result_right[1]);
        result[3] = Math.max(root.val, Math.max(result_left[3], result_right[3]));
        result[4] = Math.min(root.val, Math.min(result_left[4], result_right[4]));
        return result;
    }
}
</pre>
<p>[/expand]</p>
