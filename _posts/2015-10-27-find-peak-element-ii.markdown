---
layout: post
title: Find Peak Element II
date: 2015-10-27 11:15:26.000000000 -04:00
tags:
- Algorithm
categories:
- Divide and Conquer
author: Jason
---
<p><strong><em>There is an integer matrix which has the following features:</p>

1: The numbers in adjacent positions are different.</p>
2: The matrix has n rows and m columns.</p>
3: For all i &lt; m, A[0][i] &lt; A[1][i] &amp;&amp; A[n - 2][i] > A[n - 1][i].</p>
4: For all j &lt; n, A[j][0] &lt; A[j][1] &amp;&amp; A[j][m - 2] > A[j][m - 1].</em></strong></p>
<p><a href="http://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf">Read more</a></p>

``` java
class Solution {
    /**
     * @param A: An integer matrix
     * @return: The index of the peak
     */
    public List<integer> findPeakII(int[][] A) {
        // write your code here
        List<integer> result = new ArrayList<integer>();
        if (A == null || A.length == 0) return result;
        
        for (int i = 1; i < A.length - 1; i++) {//第一行和最后一行不用考虑
            int lo = 0, hi = A[0].length - 1;
            while (lo <= hi) {
                int mid = lo + (hi - lo) / 2;
                if (A[i][mid] < A[i][mid + 1]) {
                    lo = mid + 1;
                } else if (A[i][mid] < A[i][mid - 1]) {
                    hi = mid - 1;
                } else {
                    if (A[i][mid] > A[i - 1][mid] && A[i][mid] > A[i + 1][mid]) {
                        result.add(i);
                        result.add(mid);
                        return result;
                    }
                    break;
                }
            }
        }
        return result;
    }
}
```
``` java
class Solution {
    public static List<integer> findPeakII(int[][] A) {
        // write your code here
        List<integer> result = new ArrayList<integer>();
        if (A == null || A.length == 0) return result;

        helper(A, 0, A.length - 1,result);
        return result;
    }

    public static void helper(int[][] A, int up, int down, List<integer> result) {
        if (up > down) return;
        if (up == down) {
            int j = find(A[up]);
            result.add(up);
            result.add(j);
            return;
        }
        int mid = (up + down) / 2;
        int j = find(A[mid]);//peak element for mid row
        if (A[mid][j] < A[mid - 1][j]) {
            helper(A, up, mid - 1, result);
        } else if (A[mid][j] < A[mid + 1][j]) {
            helper(A, mid + 1, down, result);
        } else {
            result.add(mid);
            result.add(j);
            return;
        }
    }

    public static int find(int[] A) {
        int lo = 0, hi = A.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (A[mid] < A[mid + 1]) {
                lo = mid + 1;
            } else if (A[mid] < A[mid - 1]) {
                hi = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
```
