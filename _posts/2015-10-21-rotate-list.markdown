---
layout: post
title: Rotate List
date: 2015-10-21 14:35:50.000000000 -04:00
type: post
published: true
status: publish
categories:
- LinkedList
tags:
- LinkedList
meta:
  _spost_short_title: ''
  _wpas_done_all: '1'
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464055225;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:592;}i:1;a:1:{s:2:"id";i:290;}i:2;a:1:{s:2:"id";i:244;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a list, rotate the list to the right by k places, where k is non-negative.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param head: the List
     * @param k: rotate to the right k places
     * @return: the list after rotation
     */
    public ListNode rotateRight(ListNode head, int k) {
        // write your code here
        if (head == null) return null;
        int len = getSize(head);
        k %= len;
        ListNode prev = head, right = head;
        for (int i = 0; i < len - k; i++) {//we can find the nth node from the end use len directly, since we already calculate it
            prev = right;
            right = right.next;
        }
        if (right == null) { //!!important corner case
            return head;
        }
        prev.next = null;
        ListNode tail = right;
        while (tail.next != null) {
            tail = tail.next;
        }
        tail.next = head;
        return right;
    }    
    public int getSize(ListNode head) {
        int count = 0;
        while (head != null) {
            head = head.next;
            count ++;
        }
        return count;
    }
}
</pre>
<p>[/expand]</p>
