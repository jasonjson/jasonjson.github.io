#!/usr/local/bin/python3

# -*- coding: utf-8 -*-
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if not n:
            return []

        ret = [0]
        for i in xrange(n):
            mask = 1 << i
            print ret
            for j in reversed(xrange(len(ret))):
                ret.append(ret[j] | mask)
        return ret

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.grayCode(0))
