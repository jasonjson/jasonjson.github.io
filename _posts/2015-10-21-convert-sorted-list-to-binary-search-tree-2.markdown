---
layout: post
title: Convert Sorted List to Binary Search Tree
date: 2015-10-21 03:00:01.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
- LinkedList
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469091078;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:47;}i:1;a:1:{s:2:"id";i:596;}i:2;a:1:{s:2:"id";i:1085;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @return: a tree node
     */
    public TreeNode sortedListToBST(ListNode head) {  
        // write your code here
        if (head == null) return null;
        ListNode right = head, fast = head, prev = null;
        while (fast != null && fast.next != null) {
            prev = right;
            right = right.next;
            fast = fast.next.next;
        }
        TreeNode root = new TreeNode(right.val);
        if (prev != null) {//一定要单独考虑prev == null的情况
            prev.next = null;
            root.left = sortedListToBST(head);
            root.right = sortedListToBST(right.next);
        } 
        return root;
    }
}
</pre>
<p>[/expand]<br />
[expand title = "code2"]</p>
<pre>
public class Solution {
    public static ListNode h;
    public TreeNode sortedListToBST(ListNode head) { 
        if (head == null) return null;
        if (head.next == null) return new TreeNode(head.val);
        h = head;
        int len = 0;
        while (head != null) {
            head = head.next;
            len ++;
        }
        return sortedListToBSTUtil(0, len - 1);
    }    
    public TreeNode sortedListToBSTUtil(int start, int end) {
        if (start > end) return null;
        int mid = start + (end - start) / 2;
        TreeNode leftChild = sortedListToBSTUtil(start, mid - 1);
        TreeNode root = new TreeNode(h.val);
        h = h.next;
        root.left = leftChild;
        root.right = sortedListToBSTUtil(mid + 1, end);
        return root;
    }
}
</pre>
<p>[/expand]</p>
