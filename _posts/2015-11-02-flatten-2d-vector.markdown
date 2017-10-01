---
layout: post
title: Flatten 2D Vector
date: 2015-11-02 08:17:30.000000000 -05:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
<p><strong><em>Implement an iterator to flatten a 2d vector.</em></strong></p>


``` java
public class Vector2D {
    Iterator<Integer> iterator;
    Queue<iterator> q = new LinkedList<iterator>();//用queue比用ArrayList方便
    public Vector2D(List<List<Integer>> vec2d) {
        for (List<Integer> vec : vec2d) {
            q.offer(vec.iterator());
        }
        if (!q.isEmpty()) {
            iterator = q.poll();
        }
    }

    public int next() {
        if (hasNext()) {
            return iterator.next();
        } else {
            return -1;
        }
    }

    public boolean hasNext() {
        if (iterator == null) return false;
        while (!iterator.hasNext() && !q.isEmpty()) {
            iterator = q.poll();
        }
        return iterator.hasNext();
    }
}
```
