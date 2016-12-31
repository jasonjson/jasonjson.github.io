---
layout: post
title: Reverse Linked List
date: 2015-10-21 02:46:08.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467903248;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:603;}i:1;a:1:{s:2:"id";i:238;}i:2;a:1:{s:2:"id";i:1850;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Reverse a singly linked list.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param head: The head of linked list.
     * @return: The new head of reversed linked list.
     */
    public ListNode reverse(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode rev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = rev;
            rev = head;
            head = next;
        }
        return rev;
    }
    //recursiton
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode rev = reverseList(head.next);
        //head.next is the last element in rev, we connect it to the first element, and clear the first element.
        head.next.next = head;
        head.next = null;
        return rev;
    }
}
</pre>
<p>[/expand]</p>
