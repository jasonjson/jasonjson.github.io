---
layout: post
title: 382 - Linked List Random Node
date: 2017-11-12
tags:
- Leetcode
categories:
- Linkedlist
author: Jason
---
**Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.**


```python
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """

        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """

        curr = self.head
        ret, i = curr.val, 1
        while curr:
            if random.randint(1, i) == 1:
                ret = curr.val
            i += 1
            curr = curr.next
        return ret
```
