---
layout: post
title: Count Univalue Subtrees
date: 2015-11-02 08:49:03.000000000 -05:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467329156;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1198;}i:1;a:1:{s:2:"id";i:254;}i:2;a:1:{s:2:"id";i:284;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary tree, count the number of uni-value subtrees. A Uni-value subtree means all nodes of the subtree have the same value with the root.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
