---
layout: post
title: Nth to Last Node in List
date: 2015-10-21 03:01:39.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468155438;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:224;}i:1;a:1:{s:2:"id";i:228;}i:2;a:1:{s:2:"id";i:238;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Find the nth to last element of a singly linked list. The minimum number of nodes in list is n.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @param n: An integer.
     * @return: Nth to last node of a singly linked list. 
     */
    ListNode nthToLast(ListNode head, int n) {
        // write your code here
        if (head == null) return null;
        
        ListNode fast = head, slow = head;
        for (int i = 0; i < n; i++) {
           fast = fast.next; 
        }
        
        while(fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        return slow;
        // 3 - 4 - 5 - 6, n = 2
        // result should be 5 not 4
    }
}
</pre>
<p>[/expand]</p>
