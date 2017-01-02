---
layout: post
title: Intersection of Two Linked Lists
date: 2015-10-21 14:46:15.000000000 -04:00
categories:
- LinkedList
author: Jason
---
<p><strong><em>Write a program to find the node at which the intersection of two singly linked lists begins.</em></strong></p>

``` java
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        ListNode A = headA, B = headB;//must create two new node, can't change headA headB
        while (A != B) {
            A = A != null ? A.next : headB;// A = A.next = null ?....wrong!!
            B = B != null ? B.next : headA;
            //必须走到null不然就在headA前加上了node形成无限循环
            //if there is no intersection, the loop stops when both A and B gets to null
            //the length of two list should be the same now!
        }
        return A;
    }
}
```
