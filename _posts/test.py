class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        ret = [[]]
        visited = [False] * len(nums)
        self.helper(nums, visited, [], ret)
        return ret[0]

    def helper(self, nums, visited, curr, ret):
        if len(curr) > len(ret[0]):
            ret.pop()
            ret.append(curr)
        for i in xrange(len(nums)):
            if not visited[i] and self.is_valid(curr, nums[i]):
                visited[i] = True
                self.helper(nums, visited, curr + [nums[i]], ret)
                visited[i] = False

    def is_valid(self, curr, candidate):
        for num in curr:
            if num % candidate != 0 and candidate % num != 0:
                return False
        return True
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.largestDivisibleSubset([1,2,4,8]))
