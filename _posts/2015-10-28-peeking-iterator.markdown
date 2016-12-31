---
layout: post
title: Peeking Iterator
date: 2015-10-28 13:34:02.000000000 -04:00
type: post
published: true
status: publish
categories:
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465326515;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1247;}i:1;a:1:{s:2:"id";i:292;}i:2;a:1:{s:2:"id";i:1163;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</integer></integer></integer></pre>
<p>[/expand]</p>
