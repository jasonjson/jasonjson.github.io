#!/usr/bin/python
# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []

        visited = set(s)
        stack = collections.deque([s])
        ret = []
        found = False
        while stack:
            curr = stack.popleft()
            if self.is_valid(curr):
                ret.append(curr)
                found = True
            if not found:
                for i, char in enumerate(curr):
                    if char == "(" or char == ")":
                        new_s = curr[:i] + curr[i+1:]
                        print new_s
                        __import__('pdb').set_trace()
                        if new_s not in visited:
                            stack.append(new_s)
                            visited.add(new_s)
        return ret

    def is_valid(self, s):
        count = 0
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
                if count < 0:
                    return False
        return count == 0

if __name__ == "__main__":
    solution = Solution()
    solution.removeInvalidParentheses("s)")
