#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

import copy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """


        if not k or not n:
            return []

        ret = []
        self.helper(1, n, k, [], ret)
        return ret

    def helper(self, start, n, k, curr, ret):
        if len(curr) == k:
            ret.append(copy.deepcopy(curr))
            return
        for i in xrange(start, n + 1):
            curr.append(i)
            self.helper(i + 1, n, k, curr, ret)
            curr.pop()

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.combine(20, 16))
