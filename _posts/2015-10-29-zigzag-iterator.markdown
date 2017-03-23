---
layout: post
title: Zigzag Iterator
date: 2015-10-29 13:51:10.000000000 -04:00
tags:
- Algorithm
categories:
- Data Structure
author: Jason
---
<p><strong><em>Given two 1d vectors, implement an iterator to return their elements alternately. For example, given two 1d vectors:</em></strong></p>

v1 = [1, 2]</p>
v2 = [3, 4, 5, 6]</p>
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].</p>
``` java
public class ZigzagIterator {
    Queue<integer> q = new LinkedList<integer>();
    public ZigzagIterator(List<integer> v1, List<integer> v2) {
       int index = 0, prev_size = 0;
       while (true) {//can deal with k lists
           if (index < v1.size()) {
               q.offer(v1.get(index));
           }
           if (index < v2.size()) {
               q.offer(v2.get(index));
           }
           index ++;
           if (q.size() == prev_size) break;//if we didn't add new elements, break
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
