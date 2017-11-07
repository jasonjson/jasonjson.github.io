def guess(num):
    if 6 > num:
        return 1
    elif 6 < num:
        return -1
    else:
        return 0
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) / 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.guessNumber(10))
