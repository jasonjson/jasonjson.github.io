#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return -1

        nums = []
        for s in tokens:
            print(nums)
            if s.isdigit() or s[1:].isdigit():
                nums.append(int(s))
            elif s == "+":
                n1, n2 = nums.pop(), nums.pop()
                nums.append(n2 + n1)
            elif s == "-":
                n1, n2 = nums.pop(), nums.pop()
                nums.append(n2 - n1)
            elif s == "*":
                n1, n2 = nums.pop(), nums.pop()
                nums.append(n1 * n2)
            elif s == "/":
                n1, n2 = nums.pop(), nums.pop()
                nums.append(n2 // n1)
        return nums.pop()


s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
