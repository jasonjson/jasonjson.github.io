#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        s += "$"
        return self.helper(s, 0)[0]


    def helper(self, s, index):
        stack = []
        num = 0
        sign = "+"
        while index < len(s):
            c = s[index]
            if c == " ":
                continue
                index += 1
            elif c.isdigit():
                num = num * 10 + int(c)
                index += 1
            elif c == "(":
                num, index = self.helper(s, index + 1)
            else:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                elif sign == ")":
                    break
                sign = c
                num = 0
                index += 1
        return sum(stack), index

s = Solution()
print(s.calculate("1+1"))
