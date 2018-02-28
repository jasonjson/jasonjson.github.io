
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        if not d:
            return ""

        d.sort(key = lambda x : (len(x), x))
        print d
        for candidate in d:
            j = 0
            for char in s:
                if j < len(candidate) and char == candidate[j]:
                    j += 1
            print candidate
            if j == len(candidate):
                return candidate
        return ""

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.findLongestWord("abpcplea", ["ale","apple","monkey","plea"]))
