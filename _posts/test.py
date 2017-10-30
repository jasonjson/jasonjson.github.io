class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0

        ord_map = {}
        for word in words:
            mask = 0
            for c in set(word):
                mask |= (1 << (ord(c) - ord("a")))
            ord_map[mask] = max(ord_map.get(mask, 0), len(word))
        return max([ord_map[x] * ord_map[y] for x in ord_map for y in ord_map if not x & y] or [0])

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
