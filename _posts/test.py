class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in xrange(n + 1)]
        for left in range(n - 1, 0, -1):
            for right in xrange(left + 1, n + 1):
                dp[left][right] = min(max(dp[left][i - 1], dp[i + 1][right]) + i for i in xrange(left, right))
        return dp[1][n]

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.getMoneyAmount(2))

