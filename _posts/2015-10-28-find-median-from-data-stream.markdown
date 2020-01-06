---
layout: post
title: 295 Find Median from Data Stream
date: 2015-10-28 16:25:11.000000000 -04:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value. Design a data structure that supports the following two operations:**

* void addNum(int num) - Add a integer number from the data stream to the data structure.
* double findMedian() - Return the median of all elements so far.

``` java
class MedianFinder {

    PriorityQueue<Integer> max = new PriorityQueue<Integer>(10, Collections.reverseOrder());
    PriorityQueue<Integer> min = new PriorityQueue<Integer>();
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
``` python
from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.max_part = []
        self.min_part = []

    def addNum(self, num: int) -> None:
        self.count += 1
        if not self.max_part or num > self.max_part[0]:
            heappush(self.max_part, num)
        else:
            heappush(self.min_part, -num)

        if len(self.min_part) > len(self.max_part):
            heappush(self.max_part, -heappop(self.min_part))
        if len(self.max_part) > len(self.min_part) + 1:
            heappush(self.min_part, -heappop(self.max_part))
    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (self.max_part[0] - self.min_part[0]) / 2
        else:
            return self.max_part[0]
```
