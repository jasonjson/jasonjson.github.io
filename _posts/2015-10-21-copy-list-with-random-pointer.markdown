---
layout: post
title: 138 - Copy List with Random Pointer
date: 2015-10-21 02:49:30.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null. Return a deep copy of the list.**


``` java
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
```

``` python
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return
        curr = dummy = RandomListNode(0)
        dummy.next = head
        node_map = {}
        while head:
            new_head = node_map.get(head, RandomListNode(head.label))
            node_map[head] = new_head
            if head.random:
                new_random = node_map.get(head.random, RandomListNode(head.random.label))
                node_map[head.random] = new_random
                new_head.random = new_random
            curr.next = new_head
            curr = curr.next
            head = head.next
        return dummy.next
```
