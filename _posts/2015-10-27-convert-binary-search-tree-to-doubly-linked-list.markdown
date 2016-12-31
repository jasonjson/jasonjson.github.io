---
layout: post
title: Convert Binary Search Tree to Doubly Linked List
date: 2015-10-27 15:22:08.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468916766;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:596;}i:1;a:1:{s:2:"id";i:292;}i:2;a:1:{s:2:"id";i:268;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Convert a binary search tree to doubly linked list with in-order traversal.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param root: The root of tree
     * @return: the head of doubly list node
     */
    public DoublyListNode bstToDoublyList(TreeNode root) {  
        // Write your code here
        if (root == null) return null;
        ArrayList<integer> list = new ArrayList<integer>();
        Stack<treenode> stack = new Stack<treenode>();
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
        while (!stack.isEmpty()) {
            TreeNode curr = stack.pop();
            list.add(curr.val);
            if (curr.right != null) {
                curr = curr.right;
                while (curr != null) {
                    stack.push(curr);
                    curr = curr.left;
                }
            }
        }
        DoublyListNode dummy = new DoublyListNode(0);
        DoublyListNode curr = dummy;
        DoublyListNode prev = null;
        for (int n : list) {
            curr.next = new DoublyListNode(n);
            curr.prev = prev;
            prev = curr;
            curr = curr.next;
        }
        return dummy.next;
    }
}
</treenode></treenode></integer></integer></pre>
<p>[/expand]</p>
