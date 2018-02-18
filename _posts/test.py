import collections
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        start = ret = 0
        char_map = collections.defaultdict(int)
        for i, char in enumerate(s):
            char_map[char] += 1
            while len(char_map) > 2:
                char_map[s[start]] -= 1
                if char_map[s[start]] == 0:
                    del char_map[s[start]]
                start += 1
            ret = max(ret, i - start + 1)
        return ret

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.lengthOfLongestSubstringTwoDistinct("eceba"))
