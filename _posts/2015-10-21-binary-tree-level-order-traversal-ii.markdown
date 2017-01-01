---
layout: post
title: Binary Tree Level Order Traversal II
date: 2015-10-21 02:51:04.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464466027;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:278;}i:1;a:1:{s:2:"id";i:256;}i:2;a:1:{s:2:"id";i:1339;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).</em></strong><br />
[expand title="code"]</p>
<pre>
 public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: buttom-up level order a list of lists of integer
     */
    public ArrayList<ArrayList<integer>> levelOrderBottom(TreeNode root) {
        // write your code here
        ArrayList<ArrayList<integer>> result = new ArrayList<ArrayList<integer>>();
        if (root == null) return result;
        
        Queue<treenode> q = new LinkedList<treenode>();
        q.add(root);
        while (!q.isEmpty()) {
            int size = q.size();
            ArrayList<integer> list = new ArrayList<integer>();
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                list.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            result.add(list);
        }
        Collections.reverse(result);
        return result;
    }
}
</integer></integer></treenode></treenode></integer></integer></integer></pre>
<p>[/expand]</p>
