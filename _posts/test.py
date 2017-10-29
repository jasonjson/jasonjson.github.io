import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        edge_map = collections.defaultdict(list)
        for a, b in edges:
            edge_map[a].append(b)
            edge_map[b].append(a)

        prev = [k for k, v in edge_map.iteritems() if len(v) == 1]
        while len(prev) >= 2:
            curr = []
            for a in prev:
                for neighbor in edge_map[a]:
                    edge_map[neighbor].remove(a)
                    if len(edge_map[neighbor]) == 1:
                        curr.append(neighbor)
            print curr
            if len(curr) == 0:
                return prev
            prev = curr
        return prev
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
