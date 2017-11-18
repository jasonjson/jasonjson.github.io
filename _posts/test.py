class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # store index in stack
        stack, ret = [], [-1] * len(nums)
        for i in xrange(2 * len(nums)):
            num = nums[i % len(nums)]
            while stack and nums[stack[-1]] < num:
                ret[stack.pop()] = num
            if i < len(nums):
                stack.append(i)
        return ret

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100]))
