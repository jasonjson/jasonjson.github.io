class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in xrange(1, target + 1):
            for j in xrange(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]

        return dp[-1]
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.combinationSum4([1,2,3],4))
