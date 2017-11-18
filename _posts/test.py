class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums:
            return []

        index = 0
        while index < len(nums):
            nums[index], nums[nums[index] -1] = nums[nums[index] -1], nums[index]
            if index >= nums[index] -1:
                index += 1
        ret = []
        for i, num in enumerate(nums):
            if num != i + 1:
                ret.append(num)
        return ret
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
