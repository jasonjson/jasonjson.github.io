#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if not strs:
            return []

        sorted_strs = [sorted(s) for s in strs]
        str_dict = {}
        for i, s in enumerate(sorted_strs):
            index_list = str_dict.setdefault("".join(s), [])
            index_list.append(i)

        ret = []
        for indexes in str_dict.values():
            ret.append([strs[index] for index in indexes])
        return ret

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
