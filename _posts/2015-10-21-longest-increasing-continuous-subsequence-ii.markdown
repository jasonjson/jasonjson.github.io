---
layout: post
title: Longest Increasing Continuous subsequence II
date: 2015-10-21 12:54:21.000000000 -04:00
tags: algorithm
categories:
- Dynamic Programming
- Subarray
author: Jason
---
<p><strong><em>Give you an integer matrix (with row size n, column size m)，find the longest increasing continuous subsequence in this matrix. (The definition of the longest increasing continuous subsequence here can start at any row or column and go up/down/right/left any direction).</em></strong></p>


``` java
public class Solution {
    /**
     * @param A an integer matrix
     * @return  an integer
     */
    public int longestIncreasingContinuousSubsequenceII(int[][] A) {
        // Write your code here
        if (A == null || A.length == 0) return 0;
        int row = A.length, col = A[0].length;
        
        int[][] dp = new int[row][col];
        //dp[i][j] the longest sequence at point A[i][j]
        //must use dp, otherwise TLE
        int result = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                result = Math.max(result, helper(A, i, j, dp));
                //dp[i][j] is local_max ending in A[i][j]
                //result is global_max
            }
        }
        return result;
    }
    
    public int helper(int[][] A, int i, int j, int[][] dp) {
        int row = A.length, col = A[0].length;
        if (dp[i][j] != 0) {
            return dp[i][j];
        }
        int up = 0, down = 0, left = 0, right = 0;
        //talk with interviewer if there are duplicates in the matrix, if so, we need to add a boolean visited variable
        if (i - 1 >= 0 && A[i][j] > A[i-1][j]) up = helper(A, i-1, j, dp);
        if (i + 1 < row && A[i][j] > A[i+1][j]) down = helper(A, i+1, j, dp);
        if (j - 1 >= 0 && A[i][j] > A[i][j-1]) left = helper(A, i, j-1, dp);
        if (j + 1 < col && A[i][j] > A[i][j+1]) right = helper(A, i, j+1, dp);
        dp[i][j] = Math.max(Math.max(up, down), Math.max(left, right)) + 1;
        return dp[i][j];
    }
}
```
