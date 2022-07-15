---
layout: post
title: 1472 - Design Browser History
date: 2022-07-15
tags:
- Leetcode
categories:
- Array
author: Jason
---
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

* BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
* void visit(string url) Visits url from the current page. It clears up all the forward history.
* string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
* string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

```python
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.index + 1]
        self.history.append(url)
        self.index += 1

    def back(self, steps: int) -> str:
        self.index = max(0, self.index - steps)
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        self.index = min(len(self.history) - 1, self.index + steps)
        return self.history[self.index]
```
