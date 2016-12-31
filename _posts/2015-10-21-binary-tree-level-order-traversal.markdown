---
layout: post
title: Binary Tree Level Order Traversal
date: 2015-10-21 02:50:43.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464466017;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:258;}i:1;a:1:{s:2:"id";i:278;}i:2;a:1:{s:2:"id";i:1339;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: Level order a list of lists of integer
     */
     public ArrayList<ArrayList<integer>> levelOrder(TreeNode root){
         ArrayList<ArrayList<integer>> result = new ArrayList<ArrayList<integer>>();
         if (root == null) return result;
         
         Queue<treenode> q = new LinkedList<treenode>();
         q.add(root);
         while (!q.isEmpty()) {
            int size = q.size();
            //control when the level ends
            ArrayList<integer> list = new ArrayList<integer>();
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                list.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            result.add(list);
         }
         return result;
     }
}
</integer></integer></treenode></treenode></integer></integer></integer></pre>
<p>[/expand]</p>
