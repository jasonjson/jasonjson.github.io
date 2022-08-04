---
layout: post
title: 729 - My Calender I
date: 2020-02-04
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking. Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end. A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.) For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

```python
class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = TreeNode(start, end)
            return True
        return self.helper(start, end, self.root)

    def helper(self, start, end, curr):
        if start >= curr.end:
            if curr.right:
                return self.helper(start, end, curr.right)
            else:
                curr.right = TreeNode(start, end)
                return True
        elif end <= curr.start:
            if curr.left:
                return self.helper(start, end, curr.left)
            else:
                curr.left = TreeNode(start, end)
                return True
        else:
            return False
```

```
class MyCalendar:
    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> bool:
        index = self.search(start)
        if index > 0 and self.books[index - 1][1] > start:
            return False
        elif index < len(self.books) and self.books[index][0] < end:
            return False
        self.books.insert(index, [start, end])
        return True

    def search(self, start):
        left, right = 0, len(self.books) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.books[mid][0] == start:
                return mid
            elif self.books[mid][0] > start:
                right = mid - 1
            else:
                left = mid + 1
        return left
```
