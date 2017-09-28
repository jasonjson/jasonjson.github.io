#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if not matrix:
            return

        row, col = len(matrix), len(matrix[0])
        row_zero, col_zero = False, False

        for j in xrange(col):
            if matrix[0][j] == 0:
                row_zero = True
                break
        for i in xrange(row):
            if matrix[i][0] == 0:
                col_zero = True
                break
        for i in xrange(1, row):
            for j in xrange(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
        for i in xrange(1, row):
            for j in xrange(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    print i, j
                    matrix[i][j] == 0
        if row_zero:
            for j in xrange(col):
                matrix[0][j] = 0
        if col_zero:
            for i in xrange(row):
                matrix[i][0] = 0
        import pprint
        pprint.pprint(matrix)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]))
