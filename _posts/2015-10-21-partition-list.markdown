---
layout: post
title: Partition List
date: 2015-10-21 02:44:06.000000000 -04:00
type: post
published: true
status: publish
categories:
- LinkedList
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463643243;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:216;}i:1;a:1:{s:2:"id";i:246;}i:2;a:1:{s:2:"id";i:244;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x. You should preserve the original relative order of the nodes in each of the two partitions.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @param x: an integer
     * @return: a ListNode 
     */
    public ListNode partition(ListNode head, int x) {
        // write your code here
        if (head == null) return null;
        ListNode leftDummy = new ListNode(0);
        ListNode left = leftDummy;
        ListNode rightDummy = new ListNode(0);
        ListNode right = rightDummy;
        ListNode curr = head;
        while (curr != null) {
            if (curr.val < x) {
                left.next = curr;
                left = left.next;
            } else {
                right.next = curr;
                right = right.next;
            }
            curr = curr.next; 
        }     
        right.next = null;
        //bug: forget to clear the right.next, which causes an infinity loop
        //in the end, right.next = curr, and curr has its own next node, you need to clear this node.
        left.next = rightDummy.next;
        return leftDummy.next;
    }
}
</pre>
<p>[/expand]</p>
