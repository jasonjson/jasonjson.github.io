#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if not matrix:
            return

        top, bottom = 0, len(matrix) - 1
        while top < bottom:
            for i in xrange(len(matrix)):
                print matrix[top][i], matrix[bottom][i]
                matrix[top][i], matrix[bottom][i] = matrix[bottom][i], matrix[top][i]
            top += 1
            bottom -= 1

        import pprint
        pprint.pprint(matrix)
        for i in xrange(len(matrix)):
            for j in xrange(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.rotate([[1,2,3],[4,5,6],[7,8,9]]))
