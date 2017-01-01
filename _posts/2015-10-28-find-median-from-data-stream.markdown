---
layout: post
title: Find Median from Data Stream
date: 2015-10-28 16:25:11.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465818849;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1073;}i:1;a:1:{s:2:"id";i:606;}i:2;a:1:{s:2:"id";i:2049;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.</em></strong></p>
<p>Examples:<br />
[2,3,4] , the median is 3</p>
<p>[2,3], the median is (2 + 3) / 2 = 2.5</p>
<p>Design a data structure that supports the following two operations:</p>
<p>void addNum(int num) - Add a integer number from the data stream to the data structure.<br />
double findMedian() - Return the median of all elements so far.</p>
<p>[expand title="code"]</p>
<pre>
class MedianFinder {
    
    PriorityQueue<integer> max = new PriorityQueue<integer>(10, Collections.reverseOrder());
    PriorityQueue<integer> min = new PriorityQueue<integer>();
    int count = 0;
    // Adds a number into the data structure.
    public void addNum(int num) {
        count ++;
        if (max.isEmpty() || num < max.peek()) {
            max.offer(num);
        } else {
            min.offer(num);
        }
        if (min.size() > max.size()) {
            max.offer(min.poll());
        }
        if (max.size() > min.size() + 1) {
            min.offer(max.poll());
        }
    }

    // Returns the median of current data stream
    public double findMedian() {
        if (count % 2 == 0) {
            return (max.peek() + min.peek()) / 2.0;
        } else {
            return max.peek();
        }
    }
};
</integer></integer></integer></integer></pre>
<p>[/expand]</p>
