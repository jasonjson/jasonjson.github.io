---
layout: post
title: Copy Books
date: 2015-10-25 10:07:53.000000000 -04:00
categories:
- Brain teaser
- Dynamic Programming
author: Jason
---
<p><strong><em>Given an array A of integer with size of n( means n books and number of pages of each book) and k people to copy the book. You must distribute the continuous id books to one people to copy. (You can give book A[1],A[2] to one people, but you cannot give book A[1], A[3] to one people, because book A[1] and A[3] is not continuous.) Each person have can copy one page per minute. Return the number of smallest minutes need to copy all the books.</em></strong></p>

``` java
public class Solution {
    public int copyBooks(int[] pages, int k) {
        if (pages == null || pages.length == 0) return 0;
        
        int lo = 0, hi = 10000000;
        while (lo < hi) {//注意不是lo <= hi, 因为我们没有break的条件，不然当lo = hi = mid时 死循环
            int mid = (lo + hi) / 2;
            if (check(mid, pages, k)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
    
    public boolean check(int minute, int[] pages, int k) {//检查minute是否满足k个人读完所有书
        int sum = 0, count = 0, i = 0;
        while (i < pages.length) {
            if (sum + pages[i] <= minute) {
                sum += pages[i++];
            } else if (pages[i] <= minute) {
                count ++;//不增加i，还需要继续循环至第一个if
                sum = 0;
            } else {
                return false;
            }
        }
        if (sum != 0) {//如果最后一本书执行的是第一个sum,我们必须增加一个人读这些sum
            count ++;
        }
        return count <= k;
    }
}
```
``` java
public class Solution {
    /**
     * @param pages: an array of integers
     * @param k: an integer
     * @return: an integer
     */
    public int copyBooks(int[] pages, int k) {
        // write your code here
        if (pages == null || pages.length == 0 || k <= 0) return 0;
        
        int max_time = 0;
        int[][] dp = new int[k + 1][pages.length + 1];
        for (int j = 1; j <= pages.length; j++) {
            dp[1][j] = dp[1][j - 1] + pages[j - 1];
            max_time = Math.max(max_time, pages[j - 1]);
        }
        if (k >= pages.length) {
            return max_time;
        }
        
        for (int i = 2; i <= k; i++) {
            for (int j = i; j <= pages.length; j++) {
                int sum = 0;
                dp[i][j] = Integer.MAX_VALUE;
                for (int l = j; l >= 1; l--) {
                    sum += pages[l - 1]; 
                   //以l为界画条线，l以后的书都归最后一个人读,l以前的书归前i-1个人读
                    dp[i][j] = Math.min(dp[i][j], Math.max(dp[i - 1][l - 1], sum));
                }
            }
        }
        return dp[k][pages.length];
    }
}
```
