#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        st = []
        ans = []
        
        for x in nums:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)

        for x in findNums:
            ans.append(d.get(x, -1))
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.nextGreaterElement([4, 1, 2], [1,3,4,2]))
