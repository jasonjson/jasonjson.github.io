---
layout: post
title: Delete Node in the Middle of Singly Linked List
date: 2015-10-21 02:04:08.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
<p><strong><em>Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.</em></strong></p>


``` java
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
```
