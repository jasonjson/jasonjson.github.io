#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0
        #sell[i] 表示第i天未持股时，获得的最大利润，buy[i]表示第i天持有股票时，获得的最大利润。
        #对于sell[i]，最大利润有两种可能，一是今天没动作跟昨天未持股状态一样，二是今天卖了股票，所以状态转移方程如下：
        #sell[i] = max{sell[i - 1], buy[i-1] + prices[i]}
        #对于buy[i]，最大利润有两种可能，一是今天没动作跟昨天持股状态一样，二是前天卖了股票，今天买了股票，
        #因为 cooldown 只能隔天交易，所以今天买股票要追溯到前天的状态。状态转移方程如下：
        sell = [0] * len(prices)
        buy = [0] * len(prices)
        buy[0] = -prices[0]
        for i in xrange(1, len(prices)):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            tmp = sell[i - 2] if i > 1 else 0
            buy[i] = max(buy[i - 1], tmp - prices[i])
        import pprint
        pprint.pprint(buy)
        pprint.pprint(sell)
        return sell[-1]

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.maxProfit([1, 100, 3, 4, 5]))
