---
layout: post
title: Peeking Iterator
date: 2015-10-28 13:34:02.000000000 -04:00
categories:
- Data Structure
author: Jason
---
<p><strong><em>Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().</em></strong></p>

``` java
class PeekingIterator implements Iterator<integer> {
    Integer nextElement;
    Iterator<integer> iterator;
    public PeekingIterator(Iterator<integer> iterator) {
        // initialize any member here.
        this.iterator = iterator;
        nextElement = null;
    }

    // Returns the next element in the iteration without advancing the iterator.
    public Integer peek() {
        if (nextElement == null) {
            nextElement = iterator.next();
        }
        return nextElement;
    }

    // hasNext() and next() should behave the same as in the Iterator interface.
    // Override them if needed.
    @Override
    public Integer next() {
        if (nextElement == null) {
            return iterator.next();
        } else {
            int result = nextElement;
            nextElement = null;
            return result;
        }
    }

    @Override
    public boolean hasNext() {
        return nextElement != null || iterator.hasNext();
    }
}
```
