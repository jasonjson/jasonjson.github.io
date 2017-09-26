#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        num = 1
        ret = [[0] * n for i in xrange(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        while num <= n * n and left < right and top < bottom:
            for j in xrange(left, right + 1):
                ret[top][j] = num
                num += 1
            top += 1
            for i in xrange(top, bottom + 1):
                ret[i][right] = num
                num += 1
            right -= 1
            for j in reversed(xrange(left, right + 1)):
                ret[bottom][j] = num
                num += 1
            bottom -= 1
            for i in reversed(xrange(top, bottom + 1)):
                ret[i][left] = num
                num += 1
            left += 1
        return ret

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.generateMatrix(3))
