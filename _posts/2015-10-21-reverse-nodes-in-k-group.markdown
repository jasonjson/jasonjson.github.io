---
layout: post
title: Reverse Nodes in k-Group
date: 2015-10-21 14:42:44.000000000 -04:00
type: post
published: true
status: publish
categories:
- LinkedList
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466144874;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:601;}i:1;a:1:{s:2:"id";i:244;}i:2;a:1:{s:2:"id";i:246;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a linked list, reverse the nodes of a linked list k at a time and return its modified list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k <= 1) return head;        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        int i = 0;
        while (head != null) {
            i ++;
            if (i % k == 0) {
                prev = reverse(prev, head.next);
                //reverse the node between prev and head.next!!
                //we reverse k node one time
                head = prev.next;
            } else {//we move head forward as an ending point                
                head = head.next;
            }
        }
        return dummy.next;
    }
    public ListNode reverse(ListNode prev, ListNode next) {
    //draw a sketch for prev, last, curr and next 
        ListNode last = prev.next;
        ListNode curr = last.next;
        //next is the ending node, when curr == next, we stop!
        while (curr != next) {            
            last.next = curr.next;//last node keep going back
            //insert curr between prev and last
            curr.next = prev.next;
            prev.next = curr;            
            curr = last.next;//update curr
        }
        return last;
    }
}
</pre>
<p>[/expand]</p>
