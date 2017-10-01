---
layout: post
title: Rehashing
date: 2015-10-21 14:34:31.000000000 -04:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
<p><strong><em>The size of the hash table is not determinate at the very beginning. If the total size of keys is too large (e.g. size >= capacity / 10), we should double the size of the hash table and rehash every keys.</em></strong></p>


``` java
public class Solution {
    /**
     * @param hashTable: A list of The first node of linked list
     * @return: A list of The first node of linked list which have twice size
     */    
    public ListNode[] rehashing(ListNode[] hashTable) {
        // write your code here
        if (hashTable == null || hashTable.length == 0) return null;
        
        int capacity = hashTable.length * 2;
        ListNode[] result = new ListNode[capacity];
        for (ListNode node : hashTable) {
            while (node != null) {
                int index = (node.val % capacity + capacity) % capacity;
                if (result[index] == null) {
                    result[index] = new ListNode(node.val);
                } else {
                    ListNode head = result[index];
                    while (head.next != null) {
                        head = head.next;
                    }
                    head.next = new ListNode(node.val);
                }
                node = node.next;
            }
        }
        return result;
    }
};
```
