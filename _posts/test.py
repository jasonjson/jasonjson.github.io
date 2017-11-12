class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return 0
        dp = list(xrange(n + 2))
        dp[1] = 0
        dp[2] = 1
        for i in xrange(3, n + 2):
            if i % 2 == 0:
                dp[i] = dp[i / 2] + 1
            else:
                dp[i] = dp[i - 1] + 1

        for i in reversed(xrange(2, n + 1)):
            if i % 2 == 0:
                dp[i] = dp[i / 2] + 1
            else:
                dp[i] = min(dp[i], dp[i + 1] + 1)
        return dp[-2]

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.integerReplacement(999))
