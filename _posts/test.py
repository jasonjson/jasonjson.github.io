import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        if not matrix:
            return -1

        heap = [(matrix[0][j], 0, j) for j in xrange(len(matrix[0]))]
        while k > 1:
            curr, row, col = heapq.heappop(heap)
            if row + 1 < len(matrix):
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
            k -= 1
        return heapq.heappop(heap)[0]
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.kthSmallest([   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]], 8))
