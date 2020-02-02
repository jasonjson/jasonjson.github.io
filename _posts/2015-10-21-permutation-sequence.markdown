---
layout: post
title: 60 - Permutation Sequence
date: 2015-10-21 03:43:20.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given n and k, return the k-th permutation sequence.**
[Reference](http://blog.sina.com.cn/s/blog_eb52001d0102v1ss.html)


``` java
//1. 以某一数字开头的排列有(n-1)!个. 例如 123, 132, 以1开头的是 2!个
//2. 所以第一位数字就可以用(k-1)/(n-1)!来确定. 这里k-1的原因是，序列号我们应从0开始计算，否则在边界时无法计算。
//3. 第二位数字。假设前面取余后为m，则第二位数字是第 m/(n-2)!个未使用的数字。
//4. 不断重复2, 3, 取余并且对(n-k)!进行除法，直至计算完毕
public class Solution {
    public String getPermutation(int n, int k) {
        List<Integer> nums = new ArrayList<Integer>();
        int[] factorial = new int[n + 1];
        factorial[0] = 1;
        for (int i = 1; i <= n; i++) {
            nums.add(i);
            factorial[i] = factorial[i - 1] * i;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            int digit = (k - 1) / factorial[n - i];
            k = (k - 1) % factorial[n - i] + 1;
            sb.append(nums.remove(digit));
        }
        return sb.toString();
    }
}
```

``` python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ret = []
        k -= 1
        nums = list(xrange(1, n + 1))
        for i in reversed(xrange(n)):
            index, k = divmod(k, math.factorial(i))
            ret.append(str(nums[index]))
            del nums[index]
        return "".join(ret)
```
