import collections
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        if not n or not edges:
            return 0

        edge_map = collections.defaultdict(list)

        for (a, b) in edges:
            edge_map[a].append(b)
            edge_map[b].append(a)
        visited = set()
        queue = []
        ret = 0
        while len(visited) != n:
            if not queue:
                for i in xrange(n):
                    if i not in visited:
                        visited.add(i)
                        queue.append(i)
                        break
                ret += 1
            curr = queue.pop()
            for neighbor in edge_map[curr]:
                edge_map[neighbor].remove(curr)
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(i)
        return ret
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.countComponents(5, [[0,1],[1,2],[3,4]]))
