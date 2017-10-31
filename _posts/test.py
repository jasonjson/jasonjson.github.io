class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1

        ret = []
        coins.sort()
        self.helper(coins, [], ret, amount)
        print ret
        return max([len(i) for i in ret] or [-1])

    def helper(self, coins, curr, ret, remain):
        if remain == 0:
            ret.append(curr[:])
            return
        for coin in coins:
            if coin <= remain:
                self.helper(coins, curr + [coin], ret, remain - coin)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.coinChange([1,2], 3))
