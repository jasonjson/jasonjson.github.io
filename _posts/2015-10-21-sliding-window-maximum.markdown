---
layout: post
title: Sliding Window Maximum
date: 2015-10-21 13:01:03.000000000 -04:00
categories:
- Brain teaser
- Data Structure
- Subarray
author: Jason
---
<p><strong><em>Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving</em></strong></p>

``` java
//For Example: A = [2,1,3,4,6,3,8,9,10,12,56], w=4

//partition the array in blocks of size w=4. The last block may have less then w. 2, 1, 3, 4 | 6, 3, 8, 9 | 10, 12, 56|

//Traverse the list from start to end and calculate maxsofar. Reset max after each block boundary (of w elements). left_max[] = 2, 2, 3, 4 | 6, 6, 8, 9 | 10, 12, 56

//Similarly calculate max in future by traversing from end to start. right_max[] = 4, 4, 4, 4 | 9, 9, 9, 9 | 56, 56, 56

//now, sliding max at each position i in current window, sliding-max(i) = max{rightmax(i), leftmax(i+w-1)} sliding_max = 4, 6, 6, 8, 9, 10, 12, 56
public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: The maximum number inside the window at each moving.
     */
    public ArrayList<integer> maxSlidingWindow(int[] nums, int k) {
        ArrayList<integer> winMax = new ArrayList<integer>();
        if (nums == null || nums.length == 0 || k <= 0) return winMax;
        
        int n = nums.length;
        int[] left = new int[n];
        left[0] = nums[0];
        for (int i = 1; i < n; i++) {
            left[i] = (i % k == 0) ? nums[i] : Math.max(left[i-1], nums[i]);
        }
        
        int[] right = new int[n];
        right[n-1] = nums[n-1];
        for (int j = n - 2; j >= 0; j--) {
            right[j] = (j % k == 0) ? nums[j] : Math.max(right[j+1], nums[j]);
        }
        
        for (int i = 0; i + k <= n; i++) {
            winMax.add(Math.max(right[i], left[i + k - 1]));
        }
        return winMax;
    }
}//we can also use segment tree structure, but TLE..
```
``` java
public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: The maximum number inside the window at each moving.
     */
    public ArrayList<integer> maxSlidingWindow(int[] nums, int k) {
        ArrayList<integer> result = new ArrayList<integer>();
        if (nums == null || nums.length == 0) return result;
        
        PriorityQueue<integer> max = new PriorityQueue<integer>(10, Collections.reverseOrder());
        int start = 0;
        for (int i = 0; i < nums.length; i++) {
            max.offer(nums[i]);
            if (i + 1 >= k) {
                result.add(max.peek());
                max.remove(nums[start++]);
            }
        }
        return result;
    }
}
```
``` java
public class Solution {
    public static int[] maxWindow(int[] nums, int k) {
        //类似于用2个stack实现min的操作，此处用一个deque维持一个递减数列的index
        //We create a Dequeue, Qi of capacity k, that stores only useful elements
        //of current window of k elements. An element is useful if it is in 
        //current window and is greater than all other elements on left side of
        //it in current window. We process all array elements one by one and 
        //maintain Qi to contain useful elements of current window and these useful 
        //elements are maintained in sorted order. The element at front of the Qi 
        //is the largest and element at rear of Qi is the smallest of current window.
        int[] result = new int[nums.length - k + 1];

        Deque<integer> deque = new LinkedList<>();
        int i = 0;
        for (; i < k; i++) {
            while (!deque.isEmpty() && nums[deque.getLast()] <= nums[i]) {
                deque.removeLast();
            }
            deque.addLast(i);
        }

        for(; i < nums.length; i++) {
            result[i - k] = nums[deque.getFirst()];
            while (!deque.isEmpty() && deque.getFirst() <= i - k) {
                deque.removeFirst();
            }
            while (!deque.isEmpty() && nums[deque.getLast()] <= nums[i]) {
                deque.removeLast();
            }
            deque.addLast(i);
        }
        result[i - k] = nums[deque.getFirst()];
        return result;
    }
}
```
