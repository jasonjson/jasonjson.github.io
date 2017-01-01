---
layout: post
title: Sum Root to Leaf Numbers
date: 2015-11-06 22:04:46.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465458464;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1461;}i:1;a:1:{s:2:"id";i:1229;}i:2;a:1:{s:2:"id";i:1426;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.<br />
An example is the root-to-leaf path 1->2->3 which represents the number 123.<br />
Find the total sum of all root-to-leaf numbers.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</string></string></string></pre>
<p>[/expand]</p>
