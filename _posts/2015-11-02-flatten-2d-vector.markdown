---
layout: post
title: Flatten 2D Vector
date: 2015-11-02 08:17:30.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467327845;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1163;}i:1;a:1:{s:2:"id";i:1126;}i:2;a:1:{s:2:"id";i:292;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Implement an iterator to flatten a 2d vector.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Vector2D {
    Iterator<integer> iterator;
    Queue<iterator> q = new LinkedList<iterator>();//用queue比用ArrayList方便
    public Vector2D(List<List<integer>> vec2d) {
        for (List<integer> vec : vec2d) {
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
</integer></integer></iterator></iterator></integer></pre>
<p>[/expand]</p>
