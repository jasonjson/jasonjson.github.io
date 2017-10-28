class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 4:
            return True

        dp = [True] * (n + 1)
        for i in xrange(4, n + 1):
            if dp[i - 1] and dp[i - 2] and dp[i - 3]:
                dp[i] = False
        print [i for i, p in enumerate(dp) if not p]
        return dp[-1]

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.canWinNim(100))
