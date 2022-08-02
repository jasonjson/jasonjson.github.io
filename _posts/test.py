#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findAndReplacePattern(self, words, p):
        def F(w):
            m = {}
            //Mark the very first "index" of each character
            b = [m.setdefault(c, len(m)) for c in w]
            print(m)
            return b
        c = F(p)
        return [w for w in words if F(w) == c]

s = Solution()
print(s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
