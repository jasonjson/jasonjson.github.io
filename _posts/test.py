#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        ret = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix) - 1
        while True:
            for j in xrange(left, right + 1):
                import pdb
                pdb.set_trace()
                print top, j
                ret.append(matrix[top][j])
            top += 1
            if self.cross(left, right, top, bottom):
                break
            for i in xrange(top, bottom + 1):
                ret.append(matrix[i][right])
            right -= 1
            if self.cross(left, right, top, bottom):
                break
            for j in reversed(xrange(left, right + 1)):
                ret.append(matrix[bottom][j])
            bottom -= 1
            if self.cross(left, right, top, bottom):
                break
            for i in reversed(xrange(top, bottom + 1)):
                ret.append(matrix[i][left])
            left += 1
            if self.cross(left, right, top, bottom):
                break
        return ret

    def cross(self, left, right, top, bottom):
        return left > right or top > bottom
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.spiralOrder([[3],[2]]))
