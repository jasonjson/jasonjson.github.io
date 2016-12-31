---
layout: post
title: Linked List Cycle
date: 2015-10-21 02:45:22.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468765174;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:228;}i:1;a:1:{s:2:"id";i:220;}i:2;a:1:{s:2:"id";i:603;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a linked list, determine if it has a cycle in it. Follow up:<br />
Can you solve it without using extra space?</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        ListNode curr = head;
        ListNode runner = head;
        while(runner != null && runner.next != null) {
            head = head.next;
            runner = runner.next.next;
            if (runner == head) return true;
            //if there is cycle, this can end the while loop
            //if there is no cycle, the loop will ends automatically 
            //since runner will gets to null
        }
        return false;
    }
}
</pre>
<p>[/expand]</p>
