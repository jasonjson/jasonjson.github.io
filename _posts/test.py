class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return 0

        ret = 0
        nums.sort()
        for i in xrange(len(nums) - 2):
            # if i > 0 and nums[i] == nums[i - 1]:
                # continue
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                # if lo > i + 1 and nums[lo] == nums[lo - 1]:
                    # lo += 1
                    # continue
                # if hi < len(nums) - 1 and nums[hi] == nums[hi + 1]:
                    # hi -= 1
                    # continue
                if nums[i] + nums[lo] + nums[hi] < target:
                    ret += hi - lo
                    lo += 1
                else:
                    hi -= 1
        return ret
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.threeSumSmaller([2,0,0,2,-2],2))
