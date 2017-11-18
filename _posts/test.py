class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        if nums[0] == 0:
            dp2[0] = 1
        elif nums[0] == 1:
            dp1[0] = dp2[0] = 1

        for i in xrange(1, len(nums)):
            if nums[i] == 0:
                dp2[i] = dp1[i - 1] + 1
            elif nums[i] == 1:
                dp2[i] = dp1[i] = dp1[i - 1] + 1

        __import__('pdb').set_trace()
        return max(dp2)
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.findMaxConsecutiveOnes([1,0,1,1,0,1]))
