class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        if not nums:
            return []

        sum_list = [[0, 0]]
        for i, num in enumerate(nums):
            curr_sum = sum_list[-1][0]
            sum_list.append([curr_sum, i + 1])
        sum_list.sort(key=lambda x : x[0])
        min_sum = 2 ** 31 - 1
        start = end = -1
        __import__('pprint').pprint(sum_list)
        for i in xrange(1, len(sum_list)):
            diff = sum_list[i][0] - sum_list[i - 1][0]
            if min_sum > diff:
                start = sum_list[i - 1][1]
                end = sum_list[i][1] - 1
                min_sum = diff
        return [start, end]

if __name__ == "__main__":
    solution = Solution()
    solution.subarraySumClosest([-3,1,1,-3,5])
