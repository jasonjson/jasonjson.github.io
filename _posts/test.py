
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        citations.sort()
        lo, hi = 0, len(citations) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if self.is_valid(citations, mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

    def is_valid(self, citations, index):
        count = 0
        for citation in citations:
            if citation >= index:
                count += 1
        import pdb
        pdb.set_trace()
        return count >= index and len(citations) - count < index
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.hIndex([1]))
