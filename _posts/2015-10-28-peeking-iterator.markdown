---
layout: post
title: 284 - Peeking Iterator
date: 2015-10-28 13:34:02.000000000 -04:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().**


``` java
class PeekingIterator implements Iterator<Integer> {
    Integer nextElement;
    Iterator<Integer> iterator;
    public PeekingIterator(Iterator<Integer> iterator) {
        this.iterator = iterator;
        nextElement = null;
    }

    public Integer peek() {
        if (nextElement == null) {
            nextElement = iterator.next();
        }
        return nextElement;
    }

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

``` python
class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_element = None

    def peek(self):
        if self.next_element is None:
            self.next_element = self.iterator.next()
        return self.next_element

    def next(self):
        if self.next_element is None:
            return self.iterator.next()
        else:
            ret = self.next_element
            self.next_element = None
            return ret

    def hasNext(self):
        return self.next_element is not None or self.iterator.hasNext()
```
