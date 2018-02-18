class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        if not nums:
            return []

        ret = []
        if nums[0] > lower + 1:
            ret.append(self.helper(lower, nums[0]))
        for i in xrange(1, len(nums)):
            if nums[i] >= nums[i - 1] + 2:
                ret.append(self.helper(nums[i - 1] + 1, nums[i] - 1))
        if upper > nums[-1]:
            ret.append(self.helper(nums[-1] + 1, upper))
        return ret
    def helper(self, num1, num2):
        if num1 == num2:
            return str(num1)
        elif num1 < num2:
            return str(num1) + "->" + str(num2)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.findMissingRanges([0,1,3,50,75], 0, 99))
