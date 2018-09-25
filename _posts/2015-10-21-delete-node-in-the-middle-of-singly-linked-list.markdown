---
layout: post
title: 237 - Delete Node in the Middle of Singly Linked List
date: 2015-10-21 02:04:08.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.**


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

``` python
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        if not node:
            return

        if node.next:
            node.val = node.next.val
            node.next = node.next.next
```
