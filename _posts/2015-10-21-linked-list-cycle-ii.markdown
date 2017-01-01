---
layout: post
title: Linked List Cycle II
date: 2015-10-21 02:45:45.000000000 -04:00
type: post
published: true
status: publish
categories:
- LinkedList
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468905255;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:298;}i:1;a:1:{s:2:"id";i:246;}i:2;a:1:{s:2:"id";i:603;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a linked list, return the node where the cycle begins. If there is no cycle, return null.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @return: The node where the cycle begins. 
     *           if there is no cycle, return null
     */
    public ListNode detectCycle(ListNode head) {  
        if (head == null || head.next == null) return null;

        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                slow = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;          
        }
        return null;
    }
}
</pre>
<p>[/expand]</p>
