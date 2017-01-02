---
layout: post
title: Maximum gap
date: 2015-10-26 12:48:19.000000000 -04:00
categories:
- Brain teaser
- Integer
- Sorting
author: Jason
---
<p><strong><em>Given an unsorted array, find the maximum difference between the successive elements in its sorted form. Return 0 if the array contains less than 2 elements.</em></strong></p>


<ol>
<li>Suppose there are N elements and they range from A to B.</p>
Then the maximum gap will be no smaller than ceiling[(B - A) / (N - 1)]</p>
Let the length of a bucket to be len = ceiling[(B - A) / (N - 1)], then we will have at most num = (B - A) / len + 1 of bucket</li>
<li>For any number K in the array, we can easily find out which bucket it belongs by calculating loc = (K - A) / len and therefore maintain the maximum and minimum elements in each bucket.</p>
Since the maximum difference between elements in the same buckets will be at most len - 1, so the final answer will not be taken from two elements in the same buckets.</p>
两个bucket的距离最少是len,已经大于len - 1</li>
<li>For each non-empty buckets p, find the next non-empty buckets q, then q.min - p.max could be the potential answer to the question. Return the maximum of all those values.</li>
</ol>
``` java
class Solution {
    /**
     * @param nums: an array of integers
     * @return: the maximum difference
     */
    public int maximumGap(int[] nums) {
        if (nums == null || nums.length < 2) return 0;
        
        int maxNum = nums[0], minNum = nums[0];
        for (int n : nums) {
            maxNum = Math.max(maxNum, n);
            minNum = Math.min(minNum, n);
        }
        int len = (maxNum - minNum) / nums.length + 1;
        int[][] bucket = new int[(maxNum - minNum) / len + 1][2];
        for (int n : nums) {
            int i = (n - minNum) / len;
            if (bucket[i][0] == 0) {
                bucket[i][0] = n; //max
                bucket[i][1] = n; //min
            } else if (bucket[i][0] < n) {//update bucket
                bucket[i][0] = n;
            } else if (bucket[i][1] > n) {
                bucket[i][1] = n;
            }
        }
        int gap = Integer.MIN_VALUE, prev = 0;
        for (int i = 0; i < bucket.length; i++) {//starts from 1, 
            if (bucket[i][0] != 0) {
                gap = Math.max(gap, bucket[i][1] - bucket[prev][0]);
                prev = i;
                //the min has to be in the first bucket
                //min value in i minus max value in prev, the last bucket can be empty                
            }
        }
        return gap;
    }
}
```

``` java
class Solution {
    /**
     * @param nums: an array of integers
     * @return: the maximum difference
     */
    public int maximumGap(int[] nums) {
        // write your code here
        if (nums == null || nums.length < 2) return 0;
        
        int n = nums.length;
        Arrays.sort(nums);
        int max = Integer.MIN_VALUE;
        for (int i = 1; i < n; i++) {
            max = Math.max(max, nums[i] - nums[i-1]);
        }
        return max;
    }
}
```
