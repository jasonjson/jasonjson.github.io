#!/usr/bin/python

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True

        left, right = 0, sum(nums)
        visited = [False] * len(nums)
        return self.helper(nums, visited, left, right)

    def helper(self, nums, visited, left, right):
        if left == right:
            return True
        elif left > right:
            return False
        for i, num in enumerate(nums):
            if not visited[i]:
                visited[i] = True
                if self.helper(nums, visited, left + num, right - num):
                    return True
                else:
                    visited[i] = False
        return False

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.canPartition([1,2 ,3,5]))
