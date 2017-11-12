from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        division_map = defaultdict(list)
        for equation, value in zip(equations, values):
            division_map[equation[0]].append([equation[1], value])
            division_map[equation[1]].append([equation[0], 1.0 / value])

        return [self.helper(a, b, division_map, set()) for a, b in queries]

    def helper(self, a, b, division_map, visited):
        if a == b:
            return 1.0
        for c, v in division_map.get(a, []):
            if c == b:
                return v
            if c in visited:
                continue
            visited.add(c)
            new_v = self.helper(c, b, division_map, visited)
            visited.discard(c)
            if new_v != -1.0:
                division_map[c].append([b, new_v])
                division_map[b].append([c, 1.0 / new_v])
                return v * new_v
        return -1.0

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]))
