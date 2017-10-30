class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        primes_index = [0] * len(primes)
        num = [0] * n
        num[0] = 1
        for i in xrange(1, n):
            num[i] = min([num[primes_index[j]] * primes[j] for j in xrange(len(primes))])
            for k in xrange(len(primes)):
                if num[i] == num[primes_index[k]] * primes[k]:
                    primes_index[k] += 1

        print num
        return num[-1]
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.nthSuperUglyNumber(12, [2,7,13,19]))
