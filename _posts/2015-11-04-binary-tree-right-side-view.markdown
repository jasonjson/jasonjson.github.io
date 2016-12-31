---
layout: post
title: Binary Tree Right Side View
date: 2015-11-04 15:49:10.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"638d74641a7a3a6663f127d26f72250b";a:2:{s:7:"expires";i:1467904998;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:258;}i:1;a:1:{s:2:"id";i:278;}i:2;a:1:{s:2:"id";i:256;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution { //level order traversal
    public List<integer> rightSideView(TreeNode root) {
        List<integer> result = new ArrayList<integer>();
        if (root == null) return result;
        
        Queue<treenode> q = new LinkedList<treenode>();
        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                if (i == size - 1) {
                    result.add(curr.val);
                }
                if (curr.left != null) q.offer(curr.left);
                if (curr.right != null) q.offer(curr.right);
            }
        }
        return result;
    }
}
</treenode></treenode></integer></integer></integer></pre>
<p>[/expand]</p>
