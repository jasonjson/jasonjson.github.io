class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        if not nums1 or not nums2:
            return []


        buckets = [[] for i in xrange(max(nums1) + max(nums2) + 1)]
        for num1 in nums1:
            for num2 in nums2:
                buckets[num1 + num2].append([num1, num2])
        ret = []
        print buckets
        for bucket in buckets:
            if len(ret) < k:
                ret.extend(bucket)
        return ret
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.kSmallestPairs([1,7,11],[2,4,6],3))
