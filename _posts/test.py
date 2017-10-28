class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern or not str:
            return False

        p_map, s_map = {}, {}
        str_list = str.split(" ")
        if len(pattern) != len(str_list):
            return False
        for p, s in zip(pattern, str_list):
            __import__('pdb').set_trace()
            if p_map.get(p, s) != s or s_map.get(s, p) != p:
                return False
            print p_map, s_map
            p_map[p] = s
            s_map[s] = p
        return True
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.wordPattern("abc", "b c a"))
