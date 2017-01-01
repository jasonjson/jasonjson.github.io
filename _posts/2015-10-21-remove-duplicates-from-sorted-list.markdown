---
layout: post
title: Remove Duplicates from Sorted List
date: 2015-10-21 02:42:57.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467072227;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:218;}i:1;a:1:{s:2:"id";i:216;}i:2;a:1:{s:2:"id";i:601;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a sorted linked list, delete all duplicates such that each element appear only once.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        //if (head == null) return null; bug1 no need this, if head is null, we just return it.
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        ListNode curr = head;
        ListNode prev = null;
        while (curr != null) {
            if (!map.containsKey(curr.val)) {
                map.put(curr.val, 1);
                prev = curr;
            } else {
                prev.next = curr.next;
            }
            curr = curr.next;
        }
        return head;
    }
    
    public ListNode deleteDuplicates(ListNode head) {
        ListNode curr = head;
        while (curr != null && curr.next != null) {
            if (curr.next.val == curr.val) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }
        return head;
    }
}
</pre>
<p>[/expand]</p>
