---
layout: post
title: 281 - Zigzag Iterator
date: 2015-10-29 13:51:10.000000000 -04:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Given two 1d vectors, implement an iterator to return their elements alternately. For example, given two 1d vectors: v1 = [1, 2] v2 = [3, 4, 5, 6], by calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].**


``` java
public class ZigzagIterator {
    Queue<Integer> q = new LinkedList<Integer>();
    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
       int index = 0, prev_size = 0;
       while (true) {
           if (index < v1.size()) {
               q.offer(v1.get(index));
           }
           if (index < v2.size()) {
               q.offer(v2.get(index));
           }
           index ++;
           if (q.size() == prev_size) break;
           prev_size = q.size();
       }
    }

    public int next() {
        return q.poll();
    }

    public boolean hasNext() {
        return !q.isEmpty();
    }
}
```

``` python
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """

        self.queue = [l for l in (v1, v2) if l]


    def next(self):
        """
        :rtype: int
        """
        curr_list = self.queue.pop(0)
        val = curr_list.pop(0)
        if curr_list:
            self.queue.append(curr_list)
        return val


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.queue
```
