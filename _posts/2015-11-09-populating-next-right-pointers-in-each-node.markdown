---
layout: post
title: Populating Next Right Pointers in Each Node
date: 2015-11-09 17:36:58.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464755785;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1454;}i:1;a:1:{s:2:"id";i:596;}i:2;a:1:{s:2:"id";i:61;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p>Given a binary tree</p>
<pre><code>struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
</code></pre>
<p>Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. Initially, all next pointers are set to NULL.</p>
<p>[expand title="O(1)"]</p>
<pre>
public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null || (root.left == null && root.right == null)) return;
        root.left.next = root.right;
        if (root.next != null) root.right.next = root.next.left;
        connect(root.left);
        connect(root.right);
    }
}
</pre>
<p>[/expand]<br />
[expand title="O(n)"]</p>
<pre>
public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null) return;
        
        Queue<treelinknode> q = new LinkedList<treelinknode>();
        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            TreeLinkNode prev = null;
            for (int i = 0; i < size; i++) {
                TreeLinkNode curr = q.poll();
                if (prev != null) {
                    prev.next = curr;
                }
                prev = curr;
                if (curr.left != null) q.offer(curr.left);
                if (curr.right != null) q.offer(curr.right);
            }
        }
    }
}
</treelinknode></treelinknode></pre>
<p>[/expand]</p>
