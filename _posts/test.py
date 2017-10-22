#!/usr/bin/python

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n + 1)
        dp[1] = 1
        index2 = index3 = index5 = 1
        for i in xrange(2, n + 1):
            dp[i] = min(dp[index2] * 2, dp[index3] * 3, dp[index5] * 5)
            if dp[i] == dp[index2] * 2:
                index2 += 1
            if dp[i] == dp[index3] * 3:
                index3 += 1
            if dp[i] == dp[index5] * 5:
                index5 += 1
        print dp
        return dp[n]
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.nthUglyNumber(1))
