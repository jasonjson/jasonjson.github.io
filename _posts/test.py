class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """

        miss = 1
        ret = 0
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                print miss
                miss += miss
                ret += 1
        return ret

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.minPatches([1,5,10], 20))
