#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0

        ret = 0
        for i in xrange(len(points)):
            slope_map = {}
            same_point, same_x = 0, 1
            for j in xrange(i + 1, len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same_point += 1
                if points[i][0] == points[j][0]:
                    same_x += 1
                    continue
                slope = float(points[j][1] - points[i][1]) / float(points[j][0] - points[i][0])
                if slope in slope_map:
                    slope_map[slope] += 1
                else:
                    slope_map[slope] = 2
                ret = max(ret, same_point + slope_map[slope])
            ret = max(ret, same_x)
        return ret
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.maxPoints([[0,0],[94911151,94911150],[94911152,94911151]]))
