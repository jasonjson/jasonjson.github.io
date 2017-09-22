#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        ret = [0]
        self.helper(n, [], ret)
        return ret[0]

    def helper(self, n, cols, ret):
        if (len(cols) == n):
            import pprint
            pprint.pprint(cols)
            ret[0] += 1
            return
        for i in xrange(n):
            if self.is_valid(cols, i):
                cols.append(i)
                self.helper(n, cols, ret)
                cols.pop()

    def is_valid(self, cols, col):
        row = len(cols)
        for i in xrange(row):
            if col == cols[i]:
                return False
            elif abs(row - i) == (col - cols[i]):
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.totalNQueens(2))
