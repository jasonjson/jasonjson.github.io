---
layout: post
title: Coins in a Line III
date: 2015-10-27 14:44:26.000000000 -04:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469090116;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:480;}i:1;a:1:{s:2:"id";i:479;}i:2;a:1:{s:2:"id";i:2006;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>There are n coins in a line. Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player with the larger amount of money wins. Could you please decide the first player will win or lose?</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public boolean firstWillWin(int[] values) {
        if (values == null || values.length == 0) return false;
        int n = values.length;
        if (n <= 2) return true;
        
        int[][] dp = new int[n][n];//maximum money can get beween i and j
        int[][] sum = new int[n][n];//sum between i and j
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                sum[i][j] = i == j ? values[i] : sum[i][j-1] + values[j];
            }
        }
        
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (i == j) {
                    dp[i][j] = values[i];
                } else {
                    int min = Math.min(dp[i+1][j], dp[i][j-1]);
                    /*dp[i][j]=max(A[i]+sum[i+1][j]-dp[i+1][j], A[j]+sum[i][j-1]-dp[i][j-1])
                    A[i]+sum[i+1][j] 和 A[j]+sum[i][j-1]都等于sum[i][j],因此最后公式成为：
                    dp[i][j]=sum[i][j]-min(dp[i+1][j],dp[i][j-1])
                    画图 状态方程决定了row必须从bottom开始, col必须从左开始*/
                    dp[i][j] = sum[i][j] - min;
                }
            }
        }
        return dp[0][n-1] > sum[0][n-1] - dp[0][n-1];
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title = "recursive"]</p>
<pre>
public class Solution {
    public boolean firstWillWin(int[] values) {
        if (values.length <= 2) return true;
        return leftMoney(values, 0, values.length - 1) > 0;
    }
    
    public int leftMoney(int[] values, int start, int end) {
        if (start == end)  return values[start];
        return Math.max(values[start] - leftMoney(values, start + 1, end), values[end] - leftMoney(values, start, end - 1));
    }
}
</pre>
<p>[/expand]</p>
