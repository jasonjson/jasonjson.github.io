#!/usr/bin/python

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums:
            return []

        e1 = None
        e2 = None
        c1 = c2 = 0
        ret = []
        for num in nums:
            print e1, e2
            if c1 == 0:
                e1 = num
                c1 = 1
            elif c2 == 0 and num != e1:
                e2 = num
                c2 = 1
            else:
                if e1 == num:
                    c1 += 1
                elif e2 == num:
                    c2 += 1
                else:
                    c1 -= 1
                    c2 -= 1
        print e1, e2
        c1 = c2 = 0
        for num in nums:
            c1 += 1 if num == e1 else 0
            c2 += 1 if num == e2 else 0
        if c1 > len(nums) / 3:
            ret.append(e1)
        if c2 > len(nums) / 3:
            ret.append(e2)
        return ret
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.majorityElement([0,-1,2,-1]))
