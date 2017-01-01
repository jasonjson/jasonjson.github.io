---
layout: post
title: Copy List with Random Pointer
date: 2015-10-21 02:49:30.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1454874675;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:476;}i:1;a:1:{s:2:"id";i:1091;}i:2;a:1:{s:2:"id";i:434;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null. Return a deep copy of the list.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        RandomListNode dummy = new RandomListNode(0);
        RandomListNode curr = dummy;
        HashMap<RandomListNode, RandomListNode> map = new HashMap<>();
        while (head != null) {
            RandomListNode newNode = null;
            if (map.containsKey(head)) {
                newNode = map.get(head);
            } else {
                newNode = new RandomListNode(head.label);
                map.put(head, newNode);
            }            
            if (head.random != null) {
                if (map.containsKey(head.random)) {
                    newNode.random = map.get(head.random);
                } else {
                    newNode.random = new RandomListNode(head.random.label);
                    map.put(head.random, newNode.random);
                }
            }
            curr.next = newNode;
            curr = curr.next;
            head = head.next;
        }
        return dummy.next;
    }
}
</pre>
<p>[/expand]</p>
