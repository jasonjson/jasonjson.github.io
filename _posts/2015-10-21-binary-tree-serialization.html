---
layout: post
title: Binary Tree Serialization
date: 2015-10-21 02:57:07.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
- Data Structure
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467025968;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:595;}i:1;a:1:{s:2:"id";i:89;}i:2;a:1:{s:2:"id";i:1424;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.</em></strong><br />
[expand title="code"]</p>
<pre>
class Solution {
    public String serialize(TreeNode root) {
        StringBuilder str = new StringBuilder();
        if (root == null) return str.toString();
        serializeHelper(root, str);
        return str.toString();
    }
    
    public void serializeHelper(TreeNode root, StringBuilder str) {
        if (root == null) {
            str.append("#.");
        } else {
            str.append(root.val + ".");
            serializeHelper(root.left, str);
            serializeHelper(root.right, str);
        }
    }

    public TreeNode deserialize(String data) {
        if (data == null || data.length() == 0) return null;
        String[] strs = data.split(".");
        int[] index = new int[] {0};
        return deserializeHelper(strs, index);
    }
    
    public TreeNode deserializeHelper(String[] strs, int[] index) {
        if (index[0] == strs.length) return null;
        String next = strs[index[0]++];
        if (next.equals("#")) {
            return null;
        } else {
            TreeNode root = new TreeNode(Integer.valueOf(next));
            root.left = deserializeHelper(strs, index);
            root.right = deserializeHelper(strs, index);
            return root;
        }
    }
}
</pre>
<p>[/expand]</p>
