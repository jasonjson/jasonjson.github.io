#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return -1
        s = s + "$"
        stack = []
        sign = "+"
        num = 0
        for c in s:
            if c == " ":
                continue
            elif c.isdigit():
                num = num * 10 + int(c)
            else:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    prev = stack.pop()
                    print(prev, num)
                    a = int(prev / num)
                    stack.append(a)
                sign = c
                num = 0

        print(stack)
        return sum(stack)

s = Solution()
print(s.calculate("14-3/2"))
