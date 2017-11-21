import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not nums:
            return []

        pq = []
        start = 0
        ret = []
        for num in nums:
            heapq.heappush(pq, -num)
            print pq
            if len(pq) + 1 > k:
                min_num = heapq.heappop(pq)
                ret.append(-min_num)
                heapq.heappush(pq, min_num)
                pq.remove(-nums[start])
                start += 1
        return ret
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.maxSlidingWindow([1,3,1,2,0,5], 3))
