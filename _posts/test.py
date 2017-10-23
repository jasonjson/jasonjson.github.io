
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        nums.sort(reverse=True)
        return self.helper(nums, sum(nums) / 2, 0)

    def helper(self, nums, summation, index):
        try:
            if summation == nums[index]:
                return True
            elif summation < nums[index]:
                print summation
                return False
        except:
            import pdb
            pdb.set_trace()
        return self.helper(nums, summation - nums[index], index + 1) or self.helper(nums, summation, index + 1)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.canPartition([2,2,3,5]))
