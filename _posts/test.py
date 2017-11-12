class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0

        min_char = min(set(s), key=s.count)
        __import__('pdb').set_trace()
        if s.count(min_char) >= k:
            return len(s)
        else:
            return max(self.longestSubstring(t, k) for t in s.split(min_char))

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.longestSubstring("aaabb", 3))
