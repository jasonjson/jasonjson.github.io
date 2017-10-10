#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return ""
        nums.sort(self.comparator)
        import pprint
        pprint.pprint(nums)
        return "".join([str(num) for num in nums])

    def comparator(self, a, b):
        if str(a) + str(b) < str(b) + str(a):
            return 1
        elif str(a) + str(b) > str(b) + str(a):
            return -1
        else:
            return 0

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.largestNumber([3, 30, 34, 5, 9]))
