---
layout: post
title: 731 - My Calendar Ii
date: 2020-02-04
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking. Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end. A triple booking happens when three events have some non-empty intersection. For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

```python
class MyCalendarTwo:

    def __init__(self):
        self.single_book = []
        self.doubly_book = []


    def book(self, start: int, end: int) -> bool:
        for i, j in self.doubly_book:
            if start < j and end > i:
                return False
        for i, j in self.single_book:
            if start < j and end > i:
                self.doubly_book.append([max(start, i), min(end, j)])
        self.single_book.append([start, end])
        return True
```
