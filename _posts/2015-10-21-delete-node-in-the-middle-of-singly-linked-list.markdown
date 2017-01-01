---
layout: post
title: Delete Node in the Middle of Singly Linked List
date: 2015-10-21 02:04:08.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465365611;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:298;}i:1;a:1:{s:2:"id";i:605;}i:2;a:1:{s:2:"id";i:2039;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param node: the node in the list should be deleted
     * @return: nothing
     */
    public void deleteNode(ListNode node) {
        // write your code here
        if(node == null) return;
        if(node.next != null){
            node.val = node.next.val;
            node.next = node.next.next;
        }
    }
}
</pre>
<p>[/expand]</p>
