#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1

        while n / 2:
            x *= x
            n /= 2

        return x

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.myPow(2, 4))
