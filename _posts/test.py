#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ""

        ret = []
        index = 0
        while index < len(s):
            ret.append(s[index])
            left, right = index, index + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                print(ret)
                ret.pop()
                left -= 1
                right += 1
            index = right
            print(ret)

        return "".join(ret)

s = Solution()
print(s.removeDuplicates("aaaaaaaa"))
