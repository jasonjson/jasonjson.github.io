#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.index + 1]
        self.history.append(url)
        self.index += 1


    def back(self, steps: int) -> str:
        self.index -= steps
        if self.index < 0:
            self.inex = 0
        try:
            return self.history[self.index]
        except:
            import pdb; pdb.set_trace()

    def forward(self, steps: int) -> str:
        self.index += steps
        if self.index >= len(self.history):
            self.index = len(self.history) - 1
        return self.history[self.index]

b = BrowserHistory("leetcode.com")
b.visit("google.com")
b.visit("facebook.com")
b.visit("youtube.com")
print(b.back(1))
print(b.back(1))
print(b.forward(1))
b.visit("linkedin.com")
print(b.forward(2))
print(b.back(2))
print(b.back(7))
