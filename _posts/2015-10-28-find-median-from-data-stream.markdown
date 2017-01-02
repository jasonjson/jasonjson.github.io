---
layout: post
title: Find Median from Data Stream
date: 2015-10-28 16:25:11.000000000 -04:00
categories:
- Data Structure
author: Jason
---
<p><strong><em>Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.</em></strong></p>

<p>Examples:<br />
[2,3,4] , the median is 3</p>
<p>[2,3], the median is (2 + 3) / 2 = 2.5</p>
<p>Design a data structure that supports the following two operations:</p>
<p>void addNum(int num) - Add a integer number from the data stream to the data structure.<br />
double findMedian() - Return the median of all elements so far.</p>
``` java
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
```
